# =============================
# Student Names: Alexander Muglia, Jax Hodgkinson
# Group ID: (A1) 2
# Date: 21/01/2024
# =============================
# CISC 352 - W23
# propagators.py
# desc:
#


'''This file will contain different constraint propagators to be used within
   bt_search.

   propagator == a function with the following template
      propagator(csp, newly_instantiated_variable=None)
           ==> returns (True/False, [(Variable, Value), (Variable, Value) ...]

      csp is a CSP object---the propagator can use this to get access
      to the variables and constraints of the problem. The assigned variables
      can be accessed via methods, the values assigned can also be accessed.

      newly_instaniated_variable is an optional argument.
      if newly_instantiated_variable is not None:
          then newly_instantiated_variable is the most
           recently assigned variable of the search.
      else:
          progator is called before any assignments are made
          in which case it must decide what processing to do
           prior to any variables being assigned. SEE BELOW

       The propagator returns True/False and a list of (Variable, Value) pairs.
       Return is False if a deadend has been detected by the propagator.
       in this case bt_search will backtrack
       return is true if we can continue.

      The list of variable values pairs are all of the values
      the propagator pruned (using the variable's prune_value method).
      bt_search NEEDS to know this in order to correctly restore these
      values when it undoes a variable assignment.

      NOTE propagator SHOULD NOT prune a value that has already been
      pruned! Nor should it prune a value twice

      PROPAGATOR called with newly_instantiated_variable = None
      PROCESSING REQUIRED:
        for plain backtracking (where we only check fully instantiated
        constraints)
        we do nothing...return true, []

        for forward checking (where we only check constraints with one
        remaining variable)
        we look for unary constraints of the csp (constraints whose scope
        contains only one variable) and we forward_check these constraints.

        for gac we establish initial GAC by initializing the GAC queue
        with all constaints of the csp


      PROPAGATOR called with newly_instantiated_variable = a variable V
      PROCESSING REQUIRED:
         for plain backtracking we check all constraints with V (see csp method
         get_cons_with_var) that are fully assigned.

         for forward checking we forward check all constraints with V
         that have one unassigned variable left

         for gac we initialize the GAC queue with all constraints containing V.
   '''

from collections import defaultdict


def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no
    propagation at all. Just check fully instantiated constraints'''

    if not newVar:
        return True, []
    for c in csp.get_cons_with_var(newVar):
        # code to check if a particular assignment of all vars in a constraint satisfy the constraint
        # --------------------------------
        if c.get_n_unasgn() == 0:
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check_tuple(vals):
                return False, []
        # --------------------------------
    return True, []


def prop_FC(csp, newVar=None):
    '''Do forward checking. That is check constraints with
       only one uninstantiated variable. Remember to keep
       track of all pruned variable,value pairs and return '''

    status = False
    pruned = []

    cons = []
    if newVar is None:
        # nothing assigned yet, FC all unary cons
        cons = csp.get_all_nary_cons(1)
    else:
        # get all cons with 1 unassigned var
        cons = [x for x in csp.get_cons_with_var(
            newVar) if x.get_n_unasgn() == 1]

    for c in cons:
        var = c.get_unasgn_vars()[0]
        for pot in var.cur_domain():
            if c.check_var_val(var, pot):
                # there is at least one assignment that works
                status = True
            else:
                pruned.append((var, pot))
                var.prune_value(pot)

    # if every variable is assigned, g2g
    if len(csp.get_all_unasgn_vars()) == 0:
        status = True
    # if no constraits have only one unassigned variable, g2g
    if len(cons) == 0:
        status = True

    return status, pruned


def prop_GAC(csp, newVar=None):
    '''Do GAC propagation. If newVar is None we do initial GAC enforce
       processing all constraints. Otherwise we do GAC enforce with
       constraints containing newVar on GAC Queue'''

    status = False
    pruned = []

    cons = []
    if newVar is None:
        # Process all constraints
        cons = csp.get_all_cons()
    else:
        # Process constraints involving newVar
        cons = [x for x in csp.get_cons_with_var(
            newVar) if x.get_n_unasgn() > 0]

    def dfs(c, partial_tuple, vars_queue) -> bool:
        # DFS search to find at least 1 solution
        # Recursively assembles a tuple and then checks if valid

        # if tuple complete, check if valid
        if not vars_queue:
            return c.check_tuple(partial_tuple)

        # Keep assembling tuple
        for val in vars_queue[0].cur_domain():
            # If false, keep looking
            if dfs(c, partial_tuple + [val], vars_queue[1:]):
                return True
        return False

    for c in cons:
        for v in c.get_unasgn_vars():
            for x in v.cur_domain():
                v.assign(x)

                res = dfs(c, [], c.get_scope())

                v.unassign()

                if not res:
                    pruned.append((v, x))
                    v.prune_value(x)
                else:
                    status = True

    # if every variable is assigned, g2g
    if len(csp.get_all_unasgn_vars()) == 0:
        status = True
    # if no cons that means every constraint with current var has a full assignment, g2g
    if len(cons) == 0:
        status = True

    return status, pruned

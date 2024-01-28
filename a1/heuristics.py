# =============================
# Student Names: Alexander Muglia
# Group ID: (A1) 2
# Date: 21/01/2024
# =============================
# CISC 352 - W23
# heuristics.py
# desc: Implementation of the degree heuristic and minimum remaining value heuristic
#



'''This file will contain different constraint propagators to be used within
   the propagators

var_ordering == a function with the following template
    var_ordering(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    var_ordering returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
   '''

def ord_dh(csp):
    ''' return variables according to the Degree Heuristic '''
    vars = csp.get_all_unasgn_vars()

    ret = None
    dh = -1

    for var in vars:
        cur_dh = len(csp.get_cons_with_var(var))
        if cur_dh > dh:
            dh = cur_dh
            ret = var

    return ret

def ord_mrv(csp):
    ''' return variable according to the Minimum Remaining Values heuristic '''
    vars = csp.get_all_unasgn_vars()

    if len(vars) == 0:
        return None

    ret = vars[0]
    mrv = ret.cur_domain_size()

    for var in vars:
        var_domain_size = var.cur_domain_size()
        if var_domain_size < mrv:
            mrv = var_domain_size
            ret = var

    return ret


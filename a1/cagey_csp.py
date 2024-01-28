# =============================
# Student Names: Alexander Muglia, Jax Hodgkinson
# Group ID: (A1) 2
# Date: 21/01/2024
# =============================
# CISC 352 - W23
# cagey_csp.py
# desc:
#

#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = binary_ne_grid(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array is a list of all variables in the given csp. If you are returning an entire grid's worth of variables
they should be arranged in a linearly, where index 0 represents the top left grid cell, index n-1 represents
the top right grid cell, and index (n^2)-1 represents the bottom right grid cell. Any additional variables you use
should fall after that (i.e., the cage operand variables, if required).

1. binary_ne_grid (worth 10/100 marks)
    - A model of a Cagey grid (without cage constraints) built using only
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 10/100 marks)
    - A model of a Cagey grid (without cage constraints) built using only n-ary
      all-different constraints for both the row and column constraints.

3. cagey_csp_model (worth 20/100 marks)
    - a model of a Cagey grid built using your choice of (1) binary not-equal, or
      (2) n-ary all-different constraints for the grid, together with Cagey cage
      constraints.


Cagey Grids are addressed as follows (top number represents how the grid cells are adressed in grid definition tuple);
(bottom number represents where the cell would fall in the var_array):
+-------+-------+-------+-------+
|  1,1  |  1,2  |  ...  |  1,n  |
|       |       |       |       |
|   0   |   1   |       |  n-1  |
+-------+-------+-------+-------+
|  2,1  |  2,2  |  ...  |  2,n  |
|       |       |       |       |
|   n   |  n+1  |       | 2n-1  |
+-------+-------+-------+-------+
|  ...  |  ...  |  ...  |  ...  |
|       |       |       |       |
|       |       |       |       |
+-------+-------+-------+-------+
|  n,1  |  n,2  |  ...  |  n,n  |
|       |       |       |       |
|n^2-n-1| n^2-n |       | n^2-1 |
+-------+-------+-------+-------+

Boards are given in the following format:
(n, [cages])

n - is the size of the grid,
cages - is a list of tuples defining all cage constraints on a given grid.


each cage has the following structure
(v, [c1, c2, ..., cm], op)

v - the value of the cage.
[c1, c2, ..., cm] - is a list containing the address of each grid-cell which goes into the cage (e.g [(1,2), (1,1)])
op - a flag containing the operation used in the cage (None if unknown)
      - '+' for addition
      - '-' for subtraction
      - '*' for multiplication
      - '/' for division
      - '?' for unknown/no operation given

An example of a 3x3 puzzle would be defined as:
(3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

'''

from cspbase import *
from itertools import product
from itertools import permutations

def build_var_array(dom):
    var_array = []
    for i in dom:
        for j in dom:
            var = Variable(f"Cell({i},{j})", dom)
            var_array.append(var)
    return var_array

#returns variable corresponding to cell i,j by extracting it from the var_array
# 0-based indexing on inputs
def get_cell_from_arr(row, col, n, var_array):
    idx = n*row
    idx += col
    return var_array[idx]


def binary_ne_grid(cagey_grid):
    n, cages = cagey_grid

    cell_dom = range(1, n + 1)
    var_array = build_var_array(cell_dom)

    csp = CSP("bne", var_array)

    # all tuples x,y where x != y, 1-n
    bne_tuples = [[i, j] for (i, j) in product(range(1,n+1), repeat=2) if i != j]

    #row bne
    for row in range(n):
        for i in range(n):
            v1 = get_cell_from_arr(row, i, n, var_array)
            for j in range(i+1, n):
                v2 = get_cell_from_arr(row, j, n, var_array)

                con1 = Constraint(f"noteq Cell({row+1},{i+1}), Cell({row+1},{j+1})", [v1, v2])
                con1.add_satisfying_tuples(bne_tuples)
                con2 = Constraint(f"noteq Cell({i+1},{row+1}), Cell({j+1},{row+1})", [v2, v1])
                con2.add_satisfying_tuples(bne_tuples)

                csp.add_constraint(con1)
                csp.add_constraint(con2)

    #col bne
    for col in range(n):
        for i in range(n):
            v1 = get_cell_from_arr(i, col, n, var_array)
            for j in range(i+1, n):
                v2 = get_cell_from_arr(j, col, n, var_array)

                con1 = Constraint(f"noteq Cell({i+1},{col+1}), Cell({j+1},{col+1})", [v1, v2])
                con1.add_satisfying_tuples(bne_tuples)
                con2 = Constraint(f"noteq Cell({col+1},{i+1}), Cell({col+1},{j+1})", [v2, v1])
                con2.add_satisfying_tuples(bne_tuples)

                csp.add_constraint(con1)
                csp.add_constraint(con2)
    return csp, var_array


def nary_ad_grid(cagey_grid):
    n, cages = cagey_grid

    cell_dom = range(1, n + 1)
    var_array = build_var_array(cell_dom)

    csp = CSP("naryne", var_array)

    # all tuples x,y where x != y, 1-n
    naryne_tuples = list(permutations(cell_dom, n))

    #row ne
    for row in range(n):
        row_vars = []
        for i in range(n):
            v = get_cell_from_arr(row, i, n, var_array)
            row_vars.append(v)

        con = Constraint(f"Row {row+1} nary_ne", row_vars)
        con.add_satisfying_tuples(naryne_tuples)
        csp.add_constraint(con)

    #col ne
    for col in range(n):
        col_vars = []
        for i in range(n):
            v = get_cell_from_arr(i, col, n, var_array)
            col_vars.append(v)

        con = Constraint(f"Col {col+1} nary_ne", col_vars)
        con.add_satisfying_tuples(naryne_tuples)
        csp.add_constraint(con)

    return csp, var_array

def cagey_csp_model(cagey_grid):
    ##IMPLEMENT
    pass

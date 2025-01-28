import math_solvers.arithmetic as solver
import sympy.printing.latex as latex
if __name__ == '__main__':
    table_data = {
        "minimum_integer": 0,
        "maximum_integer": 10,
        "minimum_exponent": 1,
        "maximum_exponent": 2,
        "number_count": 5
    }

    answer = solver.order_include_exp_paren(table_data)
    print(answer)


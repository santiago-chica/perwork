import math_solvers.arithmetic as solver
import sympy.printing.latex as latex
if __name__ == '__main__':
    table_data = {
        "minimum_integer": 0,
        "maximum_integer": 10,
        "minimum_factor": 0,
        "maximum_factor": 10
    }

    answer = solver.int_div(table_data)
    print(answer)

import math_solvers.algebra as solver
import sympy.printing.latex as latex
import utils
if __name__ == '__main__':
    table_data = {
        "minimum_factor": 0,
        "maximum_factor": 10,
        "minimum_integer": 0,
        "maximum_integer": 10,
        "minimum_exponent": 0,
        "maximum_exponent": 6,
        "number_count": 5,
        "minimum_prime": 2,
        "maximum_prime": 7,
        "minimum_term_count": 3,
        "maximum_term_count": 5,
        "minimum_coefficient": -10,
        "maximum_coefficient": 10,
        "minimum_divisor": 2,
        "maximum_divisor": 13,
        "minimum_square": 1,
        "maximum_square": 4,
        "minimum_degree": 2,
        "maximum_degree": 3
    }

    answer = solver.pol_hor_axis(table_data)
    print(answer)


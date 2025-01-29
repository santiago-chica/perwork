import math_solvers.number_theory as solver
import sympy.printing.latex as latex
import utils
if __name__ == '__main__':
    table_data = {
        "minimum_factor": 0,
        "maximum_factor": 10,
        "minimum_integer": 0,
        "maximum_integer": 30,
        "minimum_exponent": 1,
        "maximum_exponent": 2,
        "number_count": 5,
        "minimum_prime": 2,
        "maximum_prime": 7,
        "minimum_factor_count": 3,
        "maximum_factor_count": 5,
        "minimum_divisor": 2,
        "maximum_divisor": 13
    }

    answer = solver.rel_prime(table_data)
    print(answer)


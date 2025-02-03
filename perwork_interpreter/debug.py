import math_solvers.statistics as solver
import sympy.printing.latex as latex
import numpy.random as rd
import numpy as np
import utils
if __name__ == '__main__':
    table_data = {
        "minimum_factor": 0,
        "maximum_factor": 5,
        "minimum_integer": 18,
        "maximum_integer": 45,
        "minimum_exponent": 0,
        "maximum_exponent": 6,
        "number_count": 5,
        "minimum_prime": 2,
        "maximum_prime": 7,
        "minimum_term_count": 3,
        "maximum_term_count": 5,
        "minimum_base": 2,
        "maximum_base": 3,
        "minimum_divisor": 2,
        "maximum_divisor": 13,
        "minimum_square": 1,
        "maximum_square": 4,
        "minimum_degree": 2,
        "maximum_degree": 3,
        "minimum_std": 1,
        "maximum_std": 3,
        "minimum_count": 3,
        "maximum_count": 10

    }
    set = solver.quartiles(table_data)
    print(set)
    print(f'Mean: {sum(set) / len(set)}')

    


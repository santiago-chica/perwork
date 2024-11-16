from sympy import solve, Eq
from sympy.abc import x, y
from numpy.random import randint, choice
from pylatex import (
    Document,
    Enumerate,
    NoEscape
)

def integerOneStepEquation(question:dict, doc:Document):

    config_table = question['configuration']

    minimum = config_table['minimum_integer']
    maximum = config_table['maximum_integer']

    domain = [i for i in range(minimum, maximum + 1) if i not in [1, 0]]
    
    solutions = []

    with doc.create(Enumerate(enumeration_symbol=r'{\alph*) }', options=NoEscape('wide, labelwidth=!, labelindent=0pt'))) as enum:
        for i in range(question['quantity']):
            equation = Eq(choice(domain) * x, choice(domain))
            solutions.append(solve(equation, x))
            enum.add_item(NoEscape(equation._repr_latex_()))
    
    print(solutions)


def parseMath(question:dict):
    return {
        "math_integer_one_step": integerOneStepEquation
    }.get(question['operation'], integerOneStepEquation)

def mathFunction():
    pass
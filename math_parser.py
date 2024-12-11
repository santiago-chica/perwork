from sympy import solve, Eq, latex
from sympy.abc import x, y
from numpy.random import randint, choice
from utils import base64Encode
from pylatex import (
    Document,
    Enumerate,
    NoEscape
)

def generic(question:dict):
    return [
        {
            'statement': question['statement'],
            'choices': question['choices'],
            'answer': question['answer']
        }
    ]

def integerOneStepEquation(question:dict):

    config_table = question['configuration']

    quantity = question['quantity']
    minimum = config_table['minimum_integer']
    maximum = config_table['maximum_integer']

    domain = [i for i in range(minimum, maximum + 1) if i not in [1, 0]]
    
    parsedQuestions = []

    for _ in range(quantity):
        equation = Eq(choice(domain) * x, choice(domain))
        statement = latex(equation, mode='equation*')
        answer = latex(solve(equation, x)[0], mode='equation*')
        parsedQuestions.append(
            {
                'statement': question['statement'] + [base64Encode(statement)],
                'choices': [[]],
                'answer': [base64Encode(answer)]
            }
        )
    return parsedQuestions

def parseQuestion(question:dict):
    return {
        'generic': generic,
        'integer_one_step_equation': integerOneStepEquation
    }.get(question['type'], generic)(question)

def obtainSheet(students, questions):
    sheet = []

    for student in students:

        studentEntry = {
            'student': student,
            'questions': []
        }
        
        for question in questions:
            parsedQuestion = parseQuestion(question)
            studentEntry['questions'].extend(parsedQuestion)
        sheet.append(studentEntry)
    return sheet

if __name__ == '__main__':
    pass
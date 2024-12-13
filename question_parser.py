from utils import base_64_encode
from math_solver import parse_math
from sympy import latex

def generic(question:dict):
    return [
        {
            'statement': question['statement'],
            'choices': question['choices'],
            'answer': question['answer']
        }
    ]

def math(question:dict):
    quantity = question['quantity']
    
    parsed_questions = []

    for _ in range(quantity):

        statement, choices, answer = parse_math(question)

        statement = latex(statement, mode='equation*', order='none')
        answer = latex(answer, mode='equation*', order='none')

        parsed_questions.append(
            {
                'statement': question['statement'] + [base_64_encode(statement)],
                'choices': [[]],
                'answer': [base_64_encode(answer)]
            }
        )

    return parsed_questions

def parse_question(question:dict):
    return {
        'generic': generic,
        'math': math
    }.get(question['type'], generic)(question)

def obtain_sheet(students, questions):
    sheet = []

    for student in students:

        student_entry = {
            'student': student,
            'questions': []
        }
        
        for question in questions:
            parsed_question = parse_question(question)
            student_entry['questions'].extend(parsed_question)
        sheet.append(student_entry)
    return sheet

if __name__ == '__main__':
    pass
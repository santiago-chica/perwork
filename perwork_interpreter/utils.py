from base64 import b64encode
from numpy.random import choice
from sympy import latex
# Encoding

def base_64_encode(txt:str):
    return b64encode(bytes(txt, 'UTF-8')).decode()

# Math solver

def get_numbers_in_range(minimum, maximum, excluded=[], quantity=1, can_repeat=True):
    
    domain = [i for i in range(minimum, maximum + 1) if i not in excluded]
    
    picked = choice(domain, size=quantity, replace=can_repeat)

    if quantity == 1:
        return picked[0]

    return picked

def format_number(number):
    if number == int(number):
        return int(number)
    return round(number, 2)

def latexify(question_tuple:tuple):
    statement, choices, answer = question_tuple

    statement = latex(statement, mode='equation*', order='none')
    answer = latex(answer, mode='equation*', order='none')

    return (statement, choices, answer)

latex_prefix = '\\begin{equation*}'
latex_sufix = '\\end{equation*}'

def string_to_tex(string:str):
    return latex_prefix + string + latex_sufix
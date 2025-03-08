from base64 import b64encode
from numpy.random import choice
from sympy import latex
from math import (
    gcd,
)
from random import(
    randint
)
# Encoding

def base_64_encode(txt:str):
    return b64encode(bytes(txt, 'UTF-8')).decode()

# Math solver

def get_numbers_in_range(minimum, maximum, excluded=[], quantity=1, can_repeat=True):
    if quantity == 0:
        return []

    domain = [i for i in range(minimum, maximum + 1) if i not in excluded]
    
    picked = choice(domain, size=quantity, replace=can_repeat)

    if quantity == 1:
        return picked[0]

    return picked

def format_number(number):
    if number == int(number):
        return int(number)
    return round(number, 2)

MAX_ATTEMPTS = 50

def coprime_number(number, max):
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        candidate = randint(1, max)
        if gcd(candidate, number) == 1:
            return candidate
    return 1

def is_prime(number):
    if number <= 1:
        return False

    for x in range(2, number):
        if not number % x:
            return False
    return True

def prime_number_list(minimum, maximum):
    return [n for n in range(max(2, minimum), maximum) if is_prime(n)]

def get_composite_and_prime(minimum, maximum):
    composites = []
    primes = []

    for n in range(max(2, minimum), maximum):
        if is_prime(n):
            primes.append(n)
        else:
            composites.append(n)

    return composites, primes

def latexify(question_tuple:tuple):
    statement, choices, answer = question_tuple

    statement = latex(statement, mode='equation*', order='none')
    answer = latex(answer, mode='equation*', order='none')
    
    return (statement, choices, answer)

latex_prefix = '\\begin{equation*}'
latex_sufix = '\\end{equation*}'

def string_to_tex(string:str):
    return latex_prefix + string + latex_sufix
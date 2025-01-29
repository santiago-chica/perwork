from numpy.random import choice
from random import choice
from math import gcd as greatest_common_divisor
from math import lcm as least_common_multiple
from utils import (
    get_numbers_in_range,
    string_to_tex,
    prime_number_list,
    get_composite_and_prime
)
# - Integers -

# Divisibility test
def divisibility(config_table:dict):
    is_divisible = choice([True, False])
    prime_factors = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])

    factor = choice(prime_factors)

    number = get_numbers_in_range(
        config_table['minimum_factor'],
        config_table['maximum_factor'],
        [0, 1]
    )

    if is_divisible:
        number *= factor
        answer = 'Es divisible'
    else:
        number = factor
        while number % factor == 0:
            number = get_numbers_in_range(
                config_table['minimum_factor'] * config_table['maximum_prime'],
                config_table['maximum_factor'] * config_table['maximum_prime'],
                [0, 1]
            )
        answer = 'No es divisible'
    

    statement = f'¿Es {number} divisible entre {factor}?'
    choices = ['Es divisible', 'No es divisible']

    return (statement, choices, answer)
# Primality test
def prime(config_table:dict):
    is_prime = choice([True, False])
    
    composites, primes = get_composite_and_prime(config_table['minimum_prime'], config_table['maximum_prime'])

    if is_prime:
        number = choice(primes)
        answer = 'Es primo'
    else:
        number = choice(composites)
        answer = 'Es compuesto'
    

    statement = f'¿Es {number} primo o compuesto?'
    choices = ['Es primo', 'Es compuesto']

    return (statement, choices, answer)
# Prime factorization
def prime_fac(config_table:dict):
    factors = []
    composite_number = 1
    factor_count = get_numbers_in_range(
        config_table['minimum_factor_count'],
        config_table['maximum_factor_count'],
        [0, 1]
    )

    primes = prime_number_list(config_table['minimum_prime'], config_table['maximum_prime'])
    for _ in range(factor_count):
        factor = choice(primes)
        composite_number *= factor
        factors.append(factor)
    
    factors.sort()

    statement = f'¿Cuáles son los factores de {composite_number}?'
    choices = []
    answer = string_to_tex(','.join([str(factor) for factor in factors]))

    return (statement, choices, answer)
# Divisors
def divisors(config_table:dict):
    number = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1]
    )

    divisors = []

    for n in range(1, number + 1):
        if number % n == 0:
            divisors.append(n)
    
    divisors.sort()

    statement = f'¿¿Cuáles son los divisores de {number}?'
    choices = []
    answer = string_to_tex(','.join([str(divisor) for divisor in divisors]))

    return (statement, choices, answer)

def two_related_numbers(config_table):
    factor = get_numbers_in_range(
        config_table['minimum_divisor'],
        config_table['maximum_divisor'],
        [0, 1]
    )

    l, r = get_numbers_in_range(
        config_table['minimum_factor'],
        config_table['maximum_factor'],
        [0, 1],
        2,
        False
    )

    l *= factor
    r *= factor
    return l,r
# Greatest common divisor
def gcd(config_table:dict):
    l, r = two_related_numbers(config_table)

    gcd = greatest_common_divisor(l, r)

    statement = f'¿Cual es el máximo común divisor entre {l} y {r}?'
    choices = []
    answer = string_to_tex(str(gcd))

    return (statement, choices, answer)
# Least common multiple
def lcm(config_table:dict):
    l, r = two_related_numbers(config_table)

    lcm = least_common_multiple(l, r)

    statement = f'¿Cual es el mínimo común múltiplo entre {l} y {r}?'
    choices = []
    answer = string_to_tex(str(lcm))

    return (statement, choices, answer)
# GCD and LCM
def gcd_lcm(config_table:dict):
    operator_array = [
        gcd,
        lcm
    ]
    operation = choice(operator_array)
    return operation(config_table)
# Relatively prime test
def rel_prime(config_table:dict):
    is_coprime = choice([True, False])

    l, r = get_numbers_in_range(
        config_table['minimum_integer'],
        config_table['maximum_integer'],
        [0, 1],
        2,
        False
    )

    MAX_ATTEMPTS = 50
    attempts = 0

    if is_coprime:
        while greatest_common_divisor(l, r) != 1 and attempts < MAX_ATTEMPTS:
            r = get_numbers_in_range(
                config_table['minimum_integer'],
                config_table['maximum_integer'],
                [0, 1]
            )
            attempts += 1
        answer = 'Verdadero'
    else:
        while greatest_common_divisor(l, r) == 1 and attempts < MAX_ATTEMPTS:
            r = get_numbers_in_range(
                config_table['minimum_integer'],
                config_table['maximum_integer'],
                [0, 1]
            )
            attempts += 1
        answer = 'Falso'
    
    if attempts > MAX_ATTEMPTS:
        l = 2
        r = 3
        answer = 'Verdadero'

    statement = f'¿Es {l} relativamente primo respecto de {r}?'
    choices = ['Verdadero', 'Falso']

    return (statement, choices, answer)
# Summary
def summary(config_table:dict):
    operator_array = [
        divisibility, # Number theory
        prime,
        prime_fac,
        divisors,
        gcd,
        lcm,
        gcd_lcm,
        rel_prime,
    ]
    operation = choice(operator_array)
    return operation(config_table)
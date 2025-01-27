from base64 import b64encode
from numpy.random import choice
# Encoding

def base_64_encode(txt:str):
    return b64encode(bytes(txt, 'UTF-8')).decode()

# Math solver

def get_numbers_in_range(minimum, maximum, excluded, quantity=1, can_repeat=True):
    
    domain = [i for i in range(minimum, maximum + 1) if i not in excluded]
    
    picked = choice(domain, size=quantity, replace=can_repeat)

    if quantity == 1:
        return picked[0]

    return picked
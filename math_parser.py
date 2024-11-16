from pylatex import (
    Document,
    Enumerate,
    NoEscape
)

def integerOneStepEquation(question:dict, doc:Document):
    with doc.create(Enumerate(enumeration_symbol=r'{\Alph*) }', options=NoEscape('wide, labelwidth=!, labelindent=0pt'))) as enum:
        for i in range(question['quantity']):
            enum.add_item(r'')


def parseMath(question:dict):
    return {
        "math_integer_one_step": integerOneStepEquation
    }.get(question['operation'], integerOneStepEquation)
from base64 import b64decode
from math_parser import parseMath
from pylatex import (
    Document,
    Math,
    NoEscape,
    Enumerate,
    UnsafeCommand
)

# Latex related functions

def listToLaTeX(list:list, doc:Document):
    for element in list:
        decodedElement = b64decode(element).decode()
        doc.append(NoEscape(decodedElement))

def listToEnumerate(list:list, doc:Document):
    with doc.create(Enumerate(enumeration_symbol=r'{\Alph*) }', options=NoEscape('wide, labelwidth=!, labelindent=0pt'))) as enum:
        for option in list:
            enum.add_item(r'')
            for element in option:
                decodedElement = b64decode(element).decode()
                doc.append(NoEscape(decodedElement))

# Type related functions

def generic(question:dict, doc:Document, questionEnum) -> None:

    if not (question['statement'] and question['choices'] and question['solution']):
        return

    questionEnum.add_item(r'')

    listToLaTeX(question['statement'], doc)
    listToEnumerate(question['choices'], doc)

def math(question:dict, doc:Document, questionEnum) -> None:
    if not (question['statement'] and question['quantity'] and question['operation']):
        return

    questionEnum.add_item(r'')

    listToLaTeX(question['statement'], doc)
    parseMath(question)(question, doc)
    

def parseQuestion(question:dict):
    return {
        'generic': generic,
        'math': math
    }.get(question['type'], generic)
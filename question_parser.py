from base64 import b64decode
from pylatex import (
    Document,
    Math,
    NoEscape,
    Enumerate,
    UnsafeCommand
)

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

def generic(question:dict, doc:Document, questionEnum):

    if not (question['statement'] and question['choices'] and question['solution']):
        return

    questionEnum.add_item(r'')

    listToLaTeX(question['statement'], doc)
    listToEnumerate(question['choices'], doc)

def mathIntegerOneStep(question:dict, doc:Document, questionEnum):
    pass

def parseQuestion(question:dict):
    return {
        'generic': generic,
        'math_integer_one_step': mathIntegerOneStep
    }.get(question['type'], generic)

if __name__ == '__main__':

    data_table = [{
        "type": "generic",
        "statement": [
            "QSBjb250aW51YWNpb24gbGEgZGVmaW5pY2lvbiBkZSBsYSBpbnRlZ3JhbCBwb3IgcGFydGVz",
            "XFtcaW50IHVkdj11di1caW50IHZkdVxd",
            "QmFzYWRvIGVuIGVzbywgcmVzdWVsdmEgbGFzIHNpZ3VpZW50ZXMgb3BlcmFjaW9uZXM="
        ],
        "choices": ["XGludCB4Y29zKHgpZHg="],
        "solution": ["XGludCB4Y29zKHgpZHg="]
    },
    {
        "type": "math_integer_one_step",
        "statement": [
            "QSBjb250aW51YWNpb24gbGEgZGVmaW5pY2lvbiBkZSBsYSBpbnRlZ3JhbCBwb3IgcGFydGVz",
            "XFtcaW50IHVkdj11di1caW50IHZkdVxd",
            "QmFzYWRvIGVuIGVzbywgcmVzdWVsdmEgbGFzIHNpZ3VpZW50ZXMgb3BlcmFjaW9uZXM="
        ],
        "equation": ["XGludCB4Y29zKHgpZHg="],
        "quantity": 2,
        "multiple_choice": True,
        "configuration": {
            "min_integer": 1,
            "max_integer": 10
        }
    }]
    
    pregunta1 = data_table[0]
    pregunta2 = data_table[1]

    parseQuestion(pregunta1)
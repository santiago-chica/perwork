from pylatex import (
    Document,
    Command,
    PageStyle,
    Head,
    Foot,
    Enumerate,
    NoEscape,
    Section,
    Package,
    Subsection,
    Math,
)
from json import load as jsonLoad
from base64 import b64decode
from pathlib import Path

# Directory related functions

EXPORT_FOLDER = 'export'

def verifyDirectories(projectStr:str):
    path = Path(EXPORT_FOLDER) / projectStr

    path.mkdir(exist_ok=True, parents=True)

    return path

# LaTeX related functions

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

# Export assignment function (LaTeX)

def exportAssignment(jsonPath:str):

    with open(jsonPath, 'r') as file:
        table_data = jsonLoad(file)

    exportFolder = verifyDirectories(table_data['project'])
    
    sheet = [
        {
            'student': 'Santiago Chica',
            'questions': [
                {
                    'statement': ["QSBjb250aW51YWNpb24gbGEgZGVmaW5pY2lvbiBkZSBsYSBpbnRlZ3JhbCBwb3IgcGFydGVz", "XFtcaW50IHVkdj11di1caW50IHZkdVxd", "QmFzYWRvIGVuIGVzbywgcmVzdWVsdmEgbGFzIHNpZ3VpZW50ZXMgb3BlcmFjaW9uZXM="],
                    'options': [["SW50ZWdyYWwgZGVmaW5pZGFcXA==","XChcaW50IHhjb3MoeClkeFwp="],["XChcaW50IHhjb3MoeClkeFwp="],["XChcaW50IHhjb3MoeClkeFwp="],["XChcaW50IHhjb3MoeClkeFwp="]],
                    'answer': ["XFtcaW50IHhjb3MoeClkeFxd"]
                }
            ]
        },
        {
            'student': 'Santiago Garzon',
            'questions': [
                {
                    'statement': ["QSBjb250aW51YWNpb24gbGEgZGVmaW5pY2lvbiBkZSBsYSBpbnRlZ3JhbCBwb3IgcGFydGVz", "XFtcaW50IHVkdj11di1caW50IHZkdVxd", "QmFzYWRvIGVuIGVzbywgcmVzdWVsdmEgbGFzIHNpZ3VpZW50ZXMgb3BlcmFjaW9uZXM="],
                    'options': [],
                    'answer': ["XFtcaW50IHhjb3MoeClkeFxd"]
                }
            ]
        }
    ]

    header = PageStyle('header', header_thickness=0.2, footer_thickness=0.2)

    for position, entry in enumerate(sheet, start=1):

        document_options = ['12pt']

        if table_data['double_column']:
            document_options.append('twocolumn')

        doc = Document(
            documentclass='article',
            document_options=document_options,
            geometry_options={'margin': '1in'}
        )

        doc.packages.append(Package('enumerate'))


        with header.create(Head("L")):
            header.append(entry['student'])

        with header.create(Head("C")):
            header.append(table_data['title'])

        with header.create(Head("R")):
            header.append(table_data['date'])

        with header.create(Foot('C')):
            header.append(Command('thepage'))

        doc.preamble.append(header)
        doc.change_document_style('header')

        doc.append(table_data['description'])

        doc.preamble.append(Command('setlength', arguments=[Command('headheight'), '15pt']))


        with doc.create(Enumerate(enumeration_symbol=r'{Question \arabic*. }', options=NoEscape('wide, labelwidth=!, labelindent=0pt'))) as enum:
            for question in entry['questions']:
                enum.add_item(r'')
                listToLaTeX(question['statement'], doc)
                listToEnumerate(question['options'], doc)
                listToLaTeX(question['answer'], doc)

                
                
        
        exportPath = exportFolder / f'{position}. {table_data["title"]} ({entry["student"]})'

        doc.generate_pdf(str(exportPath), clean_tex=False)
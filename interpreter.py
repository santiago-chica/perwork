from pylatex import (
    Document,
    Command,
    PageStyle,
    Head,
    Foot,
    Enumerate,
    NoEscape,
    Package
)
from json import load as jsonLoad
from base64 import b64decode
from pathlib import Path
from question_parser import obtain_sheet

# Directory related functions

EXPORT_FOLDER = 'export'

def verify_directories(projectStr:str):
    path = Path(EXPORT_FOLDER) / projectStr

    path.mkdir(exist_ok=True, parents=True)

    return path

# LaTeX related functions

def list_to_latex(list:list, doc:Document):
    if not list:
        return
    for element in list:
        decodedElement = b64decode(element).decode()
        doc.append(NoEscape(decodedElement))

def list_to_enumerate(list:list, doc:Document):
    if not list or not list[0]:
        return
    with doc.create(Enumerate(enumeration_symbol=r'{\Alph*) }', options=NoEscape('wide, labelwidth=!, labelindent=0pt'))) as enum:
        for option in list:
            enum.add_item(r'')
            for element in option:
                decodedElement = b64decode(element).decode()
                doc.append(NoEscape(decodedElement))

# Export assignment function (LaTeX)

def export_assignment(jsonPath:str):

    with open(jsonPath, 'r') as file:
        table_data = jsonLoad(file)

    exportFolder = verify_directories(table_data['project'])

    sheet = obtain_sheet(table_data['students'], table_data['questions'])

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
        doc.packages.append(Package('amsmath'))

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

        description = b64decode(table_data['description']).decode()
        doc.append(description)

        doc.preamble.append(Command('setlength', arguments=[Command('headheight'), '15pt']))
        enum_symbol = r'{' + NoEscape(table_data['question_keyword']) + r' \arabic*. }'
        with doc.create(Enumerate(enumeration_symbol=enum_symbol, options=NoEscape('wide, labelwidth=!, labelindent=0pt'))) as enum:
            for question in entry['questions']:
                enum.add_item(r'')
                list_to_latex(question['statement'], doc)
                list_to_enumerate(question['choices'], doc)
                list_to_latex(question['answer'], doc)

        exportPath = exportFolder / f'{position}. {table_data["title"]} ({entry["student"]})'

        doc.generate_pdf(str(exportPath), clean_tex=False)
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
from question_parser import parseQuestion

EXPORT_FOLDER = 'export'

def verifyDirectories(projectStr:str):
    path = Path(EXPORT_FOLDER) / projectStr

    path.mkdir(exist_ok=True, parents=True)

    return path

def exportAssignment(jsonPath:str):

    with open(jsonPath, 'r') as file:
        table_data = jsonLoad(file)

    exportFolder = verifyDirectories(table_data['project'])

    header = PageStyle('header', header_thickness=0.2, footer_thickness=0.2)

    for position, student in enumerate(table_data['students'], start=1):

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
            header.append(student)

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


        with doc.create(Enumerate(enumeration_symbol=r'{Question \arabic*. }', options=NoEscape('wide, labelwidth=!, labelindent=0pt'))) as questionEnum:
            for question in table_data['questions']:
                parseQuestion(question)(question, doc, questionEnum)
                
                
        
        exportPath = exportFolder / f'{position}. {table_data["title"]} ({student})'

        doc.generate_pdf(str(exportPath), clean_tex=False)
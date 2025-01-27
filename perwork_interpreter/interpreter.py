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
from zipfile import ZipFile
from base64 import b64decode
from json import load as json_load
from pathlib import Path
from question_parser import obtain_sheet
from io import BytesIO
from os import remove as remove_file

# Directory related functions

EXPORT_FOLDER = 'perwork_interpreter/export'
WORKSHEET_FOLDER = 'worksheets'
SOLVED_WORkSHEETS_FOLDER = 'solved_worksheets'
def verify_directories(project_str:str):
    path = Path(EXPORT_FOLDER)

    path.mkdir(exist_ok=True, parents=True)
    (path / WORKSHEET_FOLDER).mkdir(exist_ok=True, parents=True)
    (path / SOLVED_WORkSHEETS_FOLDER).mkdir(exist_ok=True, parents=True)
    return path

# LaTeX related functions

def list_to_latex(list:list, doc:Document):
    if not list:
        return
    for element in list:
        decoded_element = b64decode(element).decode()
        doc.append(NoEscape(decoded_element))

def list_to_enumerate(list:list, doc:Document):
    if not list or not list[0]:
        return
    with doc.create(Enumerate(enumeration_symbol=r'{\Alph*) }', options=NoEscape('wide, labelwidth=!, labelindent=0pt'))) as enum:
        for option in list:
            enum.add_item(r'')
            for element in option:
                decoded_element = b64decode(element).decode()
                doc.append(NoEscape(decoded_element))

# Export assignment function (LaTeX)

def export_assignment(table_data):
    export_folder = verify_directories(table_data['project'])


    memory_file = BytesIO()

    sheet = obtain_sheet(table_data['students'], table_data['questions'])

    header = PageStyle('header', header_thickness=0.2, footer_thickness=0.2)

    worksheet_paths = []

    iterate_assignment(table_data, export_folder, sheet, header, worksheet_paths)
    iterate_assignment(table_data, export_folder, sheet, header, worksheet_paths, answer=True)

    with ZipFile(memory_file, 'x') as zip:
        for path in worksheet_paths:
            if not path['answer']:
                zip.write(str(path['path']) + '.pdf', f"{WORKSHEET_FOLDER}/{path['file_name']}.pdf")
            else:
                zip.write(str(path['path']) + '.pdf', f"{SOLVED_WORkSHEETS_FOLDER}/{path['file_name']}.pdf")
            remove_file(str(path['path']) + '.pdf')
    return memory_file

def iterate_assignment(table_data, export_folder, sheet, header, worksheet_paths, answer=False):
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
                if answer:
                    list_to_latex(question['answer'], doc)

        file_name =f'{position}. {table_data["title"]} ({entry["student"]})'
        directory = 'worksheets' if not answer else 'solved_worksheets'
        export_path = export_folder / directory / file_name

        worksheet_paths.append({
                'path': export_path,
                'file_name': file_name,
                'answer': answer
        })

        doc.generate_pdf(str(export_path),
                         clean_tex=True,
                         compiler_args=['-interaction=nonstopmode'])


if __name__ == '__main__':
    table_data = None
    with open('proyectos/example.json', 'r') as data:
        table_data = json_load(data)

    export_assignment(table_data)
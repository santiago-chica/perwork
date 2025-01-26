from question_parser import ai_prompt
from interpreter import export_assignment
from json import load

if __name__ == '__main__':

    with open('./proyectos/example.json') as table_data:
        table_data = load(table_data)
        export_assignment(table_data)

import google.generativeai as genai
import typing_extensions as typing
from typing import List
import json
from numpy.random import shuffle
from utils import base_64_encode
from math_solver import parse_math
from sympy import latex
from os import getenv
from base64 import b64decode

api_key = getenv("gemini_api")
system_instructions = """Tienes encargado crear preguntas para una prueba. Considera lo siguiente:
1. Tienes que ser conciso y claro.
2. Siempre escribir en español.
3. No puedes repetir las preguntas.
4. En caso de escribir numeros, simbolos o formulas, hazlo en formato LaTeX."""

genai.configure(api_key=api_key)
client = genai.GenerativeModel("gemini-1.5-flash", system_instruction=system_instructions)

def generic(question:dict):
    return [
        {
            'statement': question['statement'],
            'choices': question['choices'],
            'answer': question['answer']
        }
    ]

def math(question:dict):
    quantity = question['quantity']
    
    parsed_questions = []

    for _ in range(quantity):

        statement, choices, answer = parse_math(question)

        final_statement = b64decode(question['statement']).decode() + statement

        parsed_questions.append(
            {
                'statement': base_64_encode(final_statement),
                'choices': [base_64_encode(choice) for choice in choices],
                'answer': base_64_encode(answer)
            }
        )

    return parsed_questions

def ai_prompt(question:dict):
    questions = []

    prompt = question['prompt']
    quantity = question['quantity']
    answer_count = question['answer_count']

    schema = {
        "type": "OBJECT",
        "properties": {
            "question": {"type": "STRING"},
            "correct_answer": {"type": "STRING"}
        },
        "required": ["question", "correct_answer"]
    }

    if answer_count > 1:
        for i in range(1, answer_count+1):
            schema['properties']['wrong_answer_' + str(i)] = {"type": 'STRING'}


    chat = client.start_chat(
        history=[
            {"role": "user", "parts": "El tema de las preguntas: " + prompt}
        ]
    )

    for question_number in range(1, quantity+1):
        response = chat.send_message(
            "Pregunta #" + str(question_number),
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=schema
            )
        )

        raw_json = response.text
        dictionary = json.loads(raw_json)

        question = {
            'statement': base_64_encode(dictionary['question']),
            'answer': base_64_encode(dictionary['correct_answer'])
        }

        if answer_count > 0:
            answers = [question['answer']]

        for i in range(1, answer_count):
            key = 'wrong_answer_' + str(i)
            wrong_answer = dictionary[key]
            answers.append(base_64_encode(wrong_answer))
        
        shuffle(answers)

        question['choices'] = answers
        questions.append(question)

    return questions


def parse_question(question:dict):
    return {
        'generic': generic,
        'math': math,
        'ai_prompt': ai_prompt
    }.get(question['type'], generic)(question)

def obtain_sheet(students, questions):
    sheet = []

    for student in students:

        student_entry = {
            'student': student,
            'questions': []
        }
        
        for question in questions:
            parsed_question = parse_question(question)
            student_entry['questions'].extend(parsed_question)
        sheet.append(student_entry)
    return sheet

if __name__ == '__main__':
    pass
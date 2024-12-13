from interpreter import export_assignment
from flask import Flask, request, send_file
from numpy.random import randint
from pathlib import Path

app = Flask(__name__)

@app.post('/api/convert')
def convert_json():
    try:
        json = request.get_json()
        export_assignment(json)
    except Exception:
        return {'success': False}
    
    return {'success': True}

if __name__ == '__main__':
    app.run()
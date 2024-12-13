from interpreter import export_assignment
from flask import Flask, request, send_file
from numpy.random import randint
from pathlib import Path

app = Flask(__name__)

@app.post('/api/convert')
def convert_json():
    try:
        json = request.get_json()

        memory_file = export_assignment(json)
        memory_file.seek(0)

        return send_file(
            memory_file,
            mimetype='application/zip',
            download_name='perwork'
        )

    except Exception as e:
        print(e.__str__())
        return {'success': False}

if __name__ == '__main__':
    app.run()
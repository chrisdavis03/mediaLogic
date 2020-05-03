import flask
from flask import request, jsonify
import sqlite3
import uuid
import db_util

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>mediaLogic</h1>
<p>An mediaProcessing API</p>'''

@app.route('/api/v1/initiate', methods=['POST'])
def initiate():
    task_parameters = request.get_json()
    task_id = str(uuid.uuid1())
    task_type = 'initiate'
    source_file = task_parameters.get('sourceFile')

    db_util.insertTask(task_id, task_type, source_file)
    task = db_util.printTask(task_id)

    return jsonify(task)

@app.route('/api/v1/encode', methods=['POST'])
def encode():
    task_parameters = request.get_json()
    task_id = str(uuid.uuid1())
    task_type = 'encode'
    source_file = task_parameters.get('sourceFile')

    db_util.insertTask(task_id, task_type, source_file)
    task = db_util.printTask(task_id)

    return jsonify(task)

app.run()


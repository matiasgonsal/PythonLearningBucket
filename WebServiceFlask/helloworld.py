from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/json')
def json_response():
    json_file = {
        'name': 'Matias',
        'age': 32
    }
    return json_file

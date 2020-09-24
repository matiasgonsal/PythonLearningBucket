from flask import Flask

app = Flask(__name__)


@app.route('/life_expectancy')
def get_life_expectancy():
    response = {
        'DOBERMAN': 11,
        'SHEPARD': 8,
        'RETRIEVER': 14
    }
    return response

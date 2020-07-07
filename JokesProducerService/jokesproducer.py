import pyjokes
from flask import Flask

app = Flask(__name__)

@app.route('/jokes')
def get_jokes():
    joke = pyjokes.get_joke('en')
    response = {
        'joke_str': joke
    }
    return response

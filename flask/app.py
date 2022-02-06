from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello world! This is Ian's second attempt at a Flask web app."

app.run(host='0.0.0.0', port=8000, debug=True)

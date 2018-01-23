from flask import Flask

app = Flask(__name__)

@app.route('/')

def show():
    return '<h1>hello world</h1> some name'

app.run(debug=True)

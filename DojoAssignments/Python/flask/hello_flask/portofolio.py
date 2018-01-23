from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def portofolio():
    return 'my portofolio'

@app.route('/projects')

def projects():
    return 'my projects'

@app.route('/about')

def about():
    return 'about'

app.run(debug=True)

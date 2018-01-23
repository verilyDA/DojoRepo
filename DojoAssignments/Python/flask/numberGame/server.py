from flask import Flask, redirect, request, session, render_template
import random
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    session['guess'] = random.randrange(0,101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():

    return render_template('guess.html', num = int(request.form['number']), numG = int(session['guess']))

app.run(debug=True)

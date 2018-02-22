from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = 'secret'

Email_key = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash('invalid name')
    else:
        session['name']=request.form['name']
    if len(request.form['location']) < 1:
        flash('invalid location')
    else:
        session['location']=request.form['location']
    if len(request.form['lang']) < 1:
        flash('invalid language')
    else:
        session['lang']=request.form['lang']
    if len(request.form['comment']) > 120:
        flash('comment too long, limit to 120 characters')
    else:
        session['comment']=request.form['comment']
    if len(request.form['name']) < 1 or len(request.form['location']) < 1 or len(request.form['lang']) < 1:
        return redirect('/')
    else:
        return render_template('results.html', name=session['name'], location=session['location'], lang=session['lang'], comment=session['comment'])

app.run(debug=True)

from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = 'secret'

Email_key = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['fname']) < 1:
        flash('First Name: invalid')
    else:
        session['fname']=request.form['fname']
        flash('First name accepted')
    if len(request.form['lname']) < 1:
        flash('Last Name: invalid')
    else:
        session['lname']=request.form['lname']
        flash('Last Name accepted')
    if len(request.form['email']) < 1:
        flash('Email: invalid')
    else:
        session['email']=request.form['email']
        flash('Email accepted')
    if len(request.form['pw']) < 1 or len(request.form['cpw']) < 1:
        flash('Password: invalid')
    if request.form['pw'] != request.form['cpw']:
        flash('Password: does not match')
    if request.form['pw'] == request.form['cpw']:
        pw = request.form['pw']
        if not any(pw.isupper() for p in pw):
            flash('Password: upper case letter needed')
        if not any(pw.isalnum() for p in pw):
            flash('Password: number needed')
    else:
        session['pw']=request.form['pw']
        flash('Password accepted')
    return redirect('/')

app.run(debug=True)

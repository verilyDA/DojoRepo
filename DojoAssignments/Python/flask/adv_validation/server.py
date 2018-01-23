from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_Std=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#this is a char checker
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) < 1:
        flash('invalid')
    elif not EMAIL_Std.match(request['email']):
        flash('invalid email address')
    else:
        flash('name input detected: ' + format(request.form['name']))
    return redirect('/')
app.run(debug=True)

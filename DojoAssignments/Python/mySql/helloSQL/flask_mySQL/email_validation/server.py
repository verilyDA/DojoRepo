from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'secret'

mysql = MySQLConnector(app, 'friends')

Email_key = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/newEmail', methods=['POST'])
def success():
    if not Email_key.match(request.form['email']):
        flash('invalid email address')
        return redirect('/')

    query = "INSERT INTO email (email, date) VALUES (:email, NOW())"
    data = {
            'email': request.form['email'],
        }
    mysql.query_db(query, data)
    x = mysql.query_db('select * from email')
    return render_template('success.html', email = x)

app.run(debug=True)

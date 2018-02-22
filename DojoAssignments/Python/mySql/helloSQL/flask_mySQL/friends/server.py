from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'secret'

mysql = MySQLConnector(app, 'friends')

@app.route('/')
def index():
    x = mysql.query_db('select * from friendslist')
    return render_template('index.html', friends = x)

@app.route('/newFriend', methods=['POST'])
def add():
    query = "INSERT INTO friendslist (name, age, since) VALUES (:name, :age, NOW())"
    data = {
            'name': request.form['name'],
            'age': request.form['age'],
        }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)

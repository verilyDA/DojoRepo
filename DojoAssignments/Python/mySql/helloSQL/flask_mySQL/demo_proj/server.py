from flask import Flask, render_template
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'airbnbdb6')
# an example of running a query
@app.route('/')
def index():
    x = mysql.query_db("SELECT * FROM users")
    return render_template('index.html', users = x)
app.run(debug=True)

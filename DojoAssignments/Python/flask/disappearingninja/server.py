from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjateam():
    return render_template('ninja.html', name = 'team')

@app.route('/ninja/<color>')
def ninja(color):
    if color == 'blue':
        return render_template('ninja.html', name = 'leo')
    elif color  == 'orange':
        return render_template('ninja.html', name = 'mikey')
    elif color  == 'red':
        return render_template('ninja.html', name = 'raf')
    elif color  == 'purple':
        return render_template('ninja.html', name = 'donny')
    else:
        return render_template('ninja.html', name = 'april')

app.run(debug=True)

from flask import Flask, redirect, request, session, render_template
import random
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    session['gold'] = 0
    session['acts'] = ''
    return redirect('/play')

@app.route('/play')
def play():

    return render_template('index.html', money = session['gold'], activity = session['acts'])

@app.route('/process/<name>', methods=['POST'])
def process(name):
    if name == 'farm':
        x = random.randrange(9,21)
        session['gold'] += x
        session['acts'] += 'Your trip to the farm got you ' + str(x) + ' gold'
    elif name == 'cave':
        x = random.randrange(4,11)
        session['gold'] += x
        session['acts'] += 'Your trip to the cave got you ' + str(x) + ' gold'
    elif name =='house':
        x = random.randrange(1,6)
        session['gold'] += x
        session['acts'] += 'Your trip to the house got you ' + str(x) + ' gold'
    else:
        if random.randrange(0,1) == 1:
            x = random.randrange(0,51)
            session['gold'] += x
            session['acts'] += 'Your trip to the casino got you ' + str(x) + ' gold'
        else:
            x = random.randrange(0,51)
            session['gold'] -= x
            session['acts'] += 'Your trip to the casino lost you ' + str(x) + ' gold'
    session['acts'] += '<br>'
    return redirect('/play')

app.run(debug=True)

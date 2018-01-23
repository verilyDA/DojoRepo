from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

#Form for DOJO SURVEY
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    print(name)
    return name


#shutdown code
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

app.run(debug=True)

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html', caption='people')

@app.route('/interviewers')
def interviewersPage():
    return render_template('interviewers.html')

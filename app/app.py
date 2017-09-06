from flask import Flask, render_template, redirect, url_for, jsonify
from flask import request
import logging


app = Flask(__name__)


@app.route('/')
def login():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')


@app.route('/', methods=['GET', 'POST'])
def login_or_register():
    error = None

    if request.method == 'POST':
        if request.form['login_register'] == "Login":
                return redirect(url_for('calendar'))
                # pageFunctionName='loginPage'

        elif request.form['login_register'] == "Register":
                return redirect(url_for('register'))
                # pageFunctionName='register'


@app.route('/updatecalendar', methods=['POST'])
def updatecalendar():
    content = request.json
    return jsonify({"content": content})

if __name__ == '__main__':
    # app.debug = True
    app.run(host='100.82.39.7', port=8010, debug=True)

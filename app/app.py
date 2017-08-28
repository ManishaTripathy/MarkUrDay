from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def login():
    return  render_template('index.html')


@app.route('/register')
def register():
    return 'register Page '

@app.route('/', methods=['POST'])
def login_or_register():
    error = None
    if request.method == 'POST':
        if request.form['login_register'] == "Login":
                pageFunctionName='loginPage'
        elif request.form['login_register'] == "Register":
                pageFunctionName='registerPage'
    return redirect(url_for(pageFunctionName))


if __name__ == '__main__':
    app.debug = True
    app.run()


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()  #write this to run

#to make different end points.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/harry")
def harry():
    return "<p>Hello Harry!</p>"

app.run()

#write debug=True (this will update any change that has been done). 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/harry")
def harry():
    return "<p>Hello Harry4!</p>"

app.run(debug=True)

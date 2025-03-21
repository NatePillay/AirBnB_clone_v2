#!/usr/bin/python3
"""script that starts a flask web application
 plus a few additional requirements"""

from flask import Flask

app = Flask("__name__")

@app.route('/', strict_slashes=False)
def hello():
	"""Return a greeting"""
	return ("Hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def hbnb():
	"""return a given string value"""
	return ("HBNB")

@app.route("/c/<text>", strict_slashes=False)
def c_Text(text):
	"""returns a given string + value"""
	string_text = text.replace("_"," ")
	return "C {}".format(string_text)

@app.route("/python/<text>", strict_slashes=False)
def python_Text(text='is_cool'):
	"""returns a given string + value"""
	string_text = text.replace("_"," ")
	return "Python {}".format(string_text)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=None)

#!/usr/bin/python3
"""script that starts a flask web application
 plus a few additional requirements"""

from flask import Flask, render_template

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

@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_Text(text="is_cool"):
	"""returns a given string + value"""
	string_text = text.replace("_"," ")
	return "Python {}".format(string_text)

@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
	"""display n is number if n is int"""
	if isinstance(n, int):
		return "{} is a number".formate(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n=None):
	"""display html page if number is int"""
	if isinstance(n, int):
		return render_template('5-number.html', n=n)

@app.route("number_odd_or_even/<int:n>", strict_slashes=False)
def number_direction(n=None):
	"""display an html page if number int and direction"""
	if instance(n, int):
		if n % 2 == 0:
			return render_template('6-number_odd_or_even.html', n=n, parity='even')
		else:
			return render_template('6-number_odd_or_even.html', n=n, parity='odd')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=None)

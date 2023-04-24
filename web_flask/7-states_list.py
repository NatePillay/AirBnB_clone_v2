#!/usr/bin/python3
"""script to run flask"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask("__name__")

@app.route("/states_list", strict_slashes=False)
def display_states():
	"""render state list html page to dipslay States"""
	states = storage.all()
	return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(self):
	"""method to remove current SQL ALCHEMY sess"""
	storage.close()

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)

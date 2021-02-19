# example blueprint file;
# can be thought of as seperate smaller app that is brought into the main
from flask import Blueprint, render_template

# Blueprint object takes in name of blueprint, import name, and several optional params
dateFinder = Blueprint('dateFinder', __name__, static_folder="static", template_folder="templates")

@dateFinder.route('/date-finder')
def date_finder():
	return render_template('date-finder.html')

@dateFinder.route('/home')
@dateFinder.route('/')
def home():
	return render_template('home.html')

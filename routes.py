from flask import Flask, render_template, request, url_for, flash, redirect, g, _app_ctx_stack, send_from_directory
from shop_style import *
from model import *
'''
This is the main web application to run for "Fashionable Holiday"
'''
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def landing_page():
	return render_template('landing_page.html')

@app.route('/homepage', methods=['GET', 'POST'])
def home_page():
	person = request.args['person']			# Men, Women, Children clothing
	date = request.args['date']
	location = request.args['location']
	place = location.split(", ")
	city = str(place[0])
	state = str(place[1])
	
	avgTempDict = forecast10(city, state)	# Gets temp info from model.py

	avgHigh = avgTempDict["avgHigh"]
	
	show_these = which_products(person, avgHigh) #Gets this from shopstyle.py

	return render_template('home_page.html',
		person=person,
		date=date,
		city = city,
		state = state,
		tops=show_these[0],
		bottoms = show_these[1],
		frosting = show_these[2],
		avgHigh = avgHigh
		)

if __name__ == '__main__':
    app.run(debug=True)
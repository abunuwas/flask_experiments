from flask import Flask, url_for, request, render_template, make_response, redirect, abort, escape, session

import os

from  database import db_session


app = Flask(__name__, static_url_path='')

secret_key = os.urandom(24)

app.secret_key = secret_key

@app.route('/')
def index():
	#return 'Hi Index Page'
	return render_template('hello.html')

@app.route('/hello')
def hello_world():
	if 'username' in session:
		return 'Hello World! You are looged as {}'.format(escape(session['username']))

@app.route('/user/<username>')
def show_user_profile(username):
	return render_template('hi_user.html', name=username)

@app.route('/redirector')
def redirector():
	return redirect(url_for('index'))

@app.route('/projects/')
def projects():
	return 'The projects page'

def do_login():
	return 'do_login'

def show_login_form():
	return 'login form'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('hello_world'))
		#do_login()
		return 'do_login'
	else:
		#show_login_form()
		return render_template('login_form.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()	

#Edef send_static
#url_for('static', filename='style.css')


with app.test_request_context('/hello', method='GET'):
	assert request.path == '/hello'
	assert request.method == 'GET'



with app.test_request_context():
	print(url_for('index'))
	print(url_for('projects', next='/'))

if __name__ == '__main__':
	app.run(debug=True)
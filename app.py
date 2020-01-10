import os, sys, ast, re, json, random, requests, datetime
from flask import Flask, session, render_template, request, redirect, url_for, g, flash, stream_with_context
from flask_restful import Resource, Api
from flask_cors import CORS
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "5fyCcv23UXIQg7JxWD6ah"

# REGRAS DE AUTENTICAÇÃO PARA PÁGINA DE LOGIN
@app.route('/', methods=['GET','POST'])
def index():

	if request.method == 'POST':
		# session.pop('user', None)

		valueForm = request.form['value']
		print(valueForm)

		try:
			num = int(valueForm)
			factorial = 1
			# check if the number is negative, positive or zero
			if num < 0:
			   print("Desculpe, não podemos calcular factorial de numeros negativos.")
			   flash('Desculpe, não podemos calcular factorial de numeros negativos.', 'danger')
			elif num == 0:
			   print("O factorial de 0 e 1")
			   flash('O factorial de 0 é 1', 'info')
			else:
			   for i in range(1,num + 1):
			       factorial = factorial*i
			   print("O factorial do numero ",num," e ",factorial)
			   # flash('O fatorial de ' + num + ' é '+ factorial, 'info')
			   flash('O factorial de 0 é 1', 'info')
			   # flash('o fatorial de ' + num + ' é ' + factorial + '.', 'info')

		except Exception as error_message:
			return redirect(url_for('index'))

	return render_template('index.html')

# REGRA PARA PÁGINA DE LOGOUT
# @app.route("/logout", methods=['GET','POST'])
# def logout():
# 	if 'user' in session:
# 		g.user = None
# 		try:
# 			dropsession()
# 			return redirect(url_for('index'))			
# 		except Exception as e:
# 			return redirect(url_for('index'))

# 	return 'Not logged in'

# @app.before_request
# def before_request():
# 	g.user = None
# 	if 'user' in session:
# 		g.user = session['user']

# @app.route('/getsession')
# def getsession():
# 	if 'user' in session:
# 		return session['user']

# 	return 'Not logged in'

# @app.route('/dropsession')
# def dropsession():
# 	session.pop('user', None)
# 	return 'Dropped!'


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port="5000")
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

@app.route('/', methods=['GET','POST'])
def index():

	if request.method == 'POST':

		valueForm = request.form['value']

		try:
			num = int(valueForm)
			factorial = 1
			if num < 0:
			   flash('Desculpe, não podemos calcular factorial de numeros negativos.', 'danger')
			   dropsession()
			elif num == 0:
			   flash('O factorial de 0 é 1', 'info')
			   dropsession()
			else:
			   for i in range(1,num + 1):
			       factorial = factorial*i
			   flash('o fatorial de ' + str(num) + ' é ' + str(factorial) + '.', 'info')
			   dropsession()

		except Exception as error_message:
			return redirect(url_for('index'))

	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port="5000")
import os, sys, ast, re, json, random, requests, datetime
from flask import Flask, session, render_template, request, redirect, url_for, g
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_mysqldb import MySQL
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = "flash message"

# REGRAS DE AUTENTICAÇÃO PARA PÁGINA DE LOGIN
@app.route('/', methods=['POST'])
def index():

	if request.method == 'POST':
		session.pop('user', None)

	    valueForm = request.form['value'] 

		try:
			num = int(valueForm)
			factorial = 1
			# check if the number is negative, positive or zero
			if num < 0:
			   print("Desculpe, não podemos calcular factorial de numeros negativos.")
			elif num == 0:
			   print("O factorial de 0 e 1")
			else:
			   for i in range(1,num + 1):
			       factorial = factorial*i
			   print("O factorial do numero ",num," e ",factorial)

		except Exception as error_message:
			return redirect(url_for('index'))

	return render_template('index.html')
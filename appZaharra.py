from flask import Flask, redirect, url_for, request
import mysql.connector as mariadb
import os
import socket

# Connect to mariadb
mariadb_conexion = mariadb.connect(host="db",
                         user='user',
                         password='pass',
                         database='Proba')
cursor = mariadb_conexion.cursor()
app = Flask(__name__)

@app.route("/db")
def db():
	pass

@app.route("/message", methods=['GET', 'POST'])
def message():
	if request.method == 'GET':
		pass #
	elif request.method == 'POST':
		pass #
	else:
		pass #errorea

@app.route("/test", methods=['GET'])
def test():
	return "ALIVE "+ socket.gethostname() #bueltatu alive eta kontainerraren id-a


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
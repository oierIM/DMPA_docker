from flask import Flask, redirect, url_for, request
import mysql.connector as mariadb
import os
import socket
import json

# Connect to mariadb
mariadb_conexion = mariadb.connect(host="db",
                         user='user',
                         password='pass',
                         database='Proba')
cursor = mariadb_conexion.cursor()
app = Flask(__name__)

@app.route("/db")
def db():
	pass #magia

@app.route("/message", methods=['GET', 'POST'])
def message():
	if request.method == 'GET':
		cursor.execute("SELECT * FROM Informazioa")
		return cursor.fetchall()
	elif request.method == 'POST':
		eskaera = request.json
		Id = socket.gethostname()
		cursor.execute(f"INSERT INTO Informazioa (From_eskaera, Content_eskaera, Id) VALUES (%s, %s, %s)",(eskaera['From'],eskaera['Content'], Id))
		cursor.execute("commit")
		return 0

@app.route("/test", methods=['GET'])
def test():
	return "ALIVE "+ socket.gethostname() #bueltatu alive eta kontainerraren id-a


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)

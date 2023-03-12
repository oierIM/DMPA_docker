from flask import Flask, redirect, url_for, request
import mysql.connector as mariadb
import os
import socket
import json

#Konexioa sortu, beharrezko host,erabiltzaile,pasahitz eta datubaseren izena pasatuz parametro bezala
mariadb_konexioa = mariadb.connect(host="db", user='user', password='pass', database='Proba') 
cursor = mariadb_konexioa.cursor()#Kontsultak egiteko beharrezkoa izango den kurtsorea sortu
app = Flask(__name__) #Flask instantzia sortu

@app.route("/db") #Adminer kontainerrera joateko eskaeraren ruta
def db():
	pass #nginx konfigurazio fitxategian berbideratzen du adminerrera iada

@app.route("/message", methods=['GET', 'POST']) #Bi metodo posible dituen message ruta, get eta post 
def message():
	if request.method == 'GET': #Datu basearen erregistro guztiak bueltatu
		cursor.execute("SELECT * FROM Informazioa") #Beharrezko taularen gainean eskaera exekutatu
		return cursor.fetchall() #Lortutako emaitzak bueltatzeko beharrezko komandoa
	elif request.method == 'POST': #Eskaeraren edukia datu basean gordeko du. Json formatuko edukia
		from_eskaera = request.json["From"] #eskaeraren edukia gordetzen dugu
		content_eskaera = request.json["Content"] #eskaeraren edukia gordetzen dugu
		id = socket.gethostname() #Uneko flask kontainerraren id-a lortu
		query = ("INSERT INTO Informazioa (From_eskaera, Content_eskaera, Id)"
               		"VALUES (%s, %s, %s)") #Gordetzeko query-a
		cursor.execute(query, (from_eskaera, content_eskaera, id)) #Exekutatu query-a
		mariadb_konexioa.commit() #Aldaketak burutu
		return "Gordeta"

@app.route("/test", methods=['GET']) #Test rutako eskaera
def test(): #ALIVE testua bueltatuko digu, bere flask kontainerraren id-arekin batera
	return "ALIVE "+ socket.gethostname() #bueltatu alive eta kontainerraren id-a


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)

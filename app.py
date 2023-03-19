from flask import Flask, redirect, url_for, request
import mysql.connector as mariadb
import os
import socket
import json

#Konexioa sortu, beharrezko host,erabiltzaile,pasahitz eta datubaseren izena pasatuz parametro bezala
mariadb_konexioa = mariadb.connect(host="db", user='user', password='pass', database='Proba')
cursor = mariadb_konexioa.cursor() #Kontsultak egiteko beharrezkoa izango den kurtsorea sortu
app = Flask(__name__) #Flask instantzia sortu

@app.route("/db") #Adminer kontainerrera joateko eskaeraren ruta
def db():
	pass #nginx konfigurazio fitxategian berbideratzen du adminerrera iada

#Bi metodo posible dituen message ruta, get eta post
@app.route("/message", methods=['GET', 'POST'])
def message():
	if request.method == 'GET': #Datu basearen erregistro guztiak bueltatu
		try:
			from_eskaera = request.args.get('From')   #eskaeraren edukia gordetzen dugu
			if str(from_eskaera) == "ALL":
				cursor.execute("SELECT * FROM Informazioa") #Beharrezko taularen gainean eskaera
				return cursor.fetchall()
			else:
				a = "SELECT * FROM Informazioa WHERE From_eskaera = '" + str(from_eskaera) + "'" #Beharrezko taularen gainean eskaera
				cursor.execute(a)
				return cursor.fetchall() #Lortutako emaitzak bueltatzeko beharrezko komandoa
		except Exception as e:
			cursor.execute("SELECT * FROM Informazioa") #Beharrezko taularen gainean eskaera
			return cursor.fetchall()
	elif request.method == 'POST': #Eskaeraren edukia datu basean gordeko du. Json formatuko edukia
		try:
			from_eskaera = request.json["From"] #eskaeraren edukia gordetzen dugu
			content_eskaera = request.json["Content"] #eskaeraren edukia gordetzen dugu
			id = socket.gethostname() #Uneko flask kontainerraren id-a lortu
			query = ("INSERT INTO Informazioa (From_eskaera, Content_eskaera, Id)"
		       		"VALUES (%s, %s, %s)") #Gordetzeko query-a
			cursor.execute(query, (from_eskaera, content_eskaera, id)) #Exekutatu query-a
			mariadb_konexioa.commit() #Aldaketak burutu
			return "Gordeta"
		except Exception as e: #Post eskaera desegoki bat tratatzeko mezua
			return ("Post eskaera desegokia izan da." 
			"Itxura honetako dei batekin saiatu: curl -d {From:AAB, Content:ttt}" 
			"-H Content Type: application/json -X POST localhost:80/message")

@app.route("/test", methods=['GET']) #Test rutako eskaera
def test(): #ALIVE testua bueltatuko digu, bere flask kontainerraren id-arekin batera
	try:
		return "ALIVE "+ socket.gethostname() #bueltatu alive eta kontainerraren id-a
	except Exception as e:
		return "Test eskaera desegokia. Itxura honetako dei batekin saiatu: localhost:80/test" #Ez da gertatuko, baina bazpadaere

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)

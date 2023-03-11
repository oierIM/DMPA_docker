from flask import Flask, redirect, url_for, request
import mysql.connector as mariadb
import os
import socket
import json

# Connect to mariadb
mariadb_konexioa = mariadb.connect(host="db", user='user', password='pass', database='Proba') #Konexioa sortu, beharrezko host,erabiltzaile,pasahitz eta datubaseren izena pasatuz parametro bezala
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
	elif request.method == 'POST': #Eskaeraren edukia datu basean gordeko du. Json formatuan egongo da edukia
		eskaera = request.json #eskaeraren edukia gordetzen dugu
		Id = socket.gethostname() #Uneko flask kontainerraren id-a lortu
		cursor.execute(f"INSERT INTO Informazioa (From_eskaera, Content_eskaera, Id) VALUES (%s, %s, %s)",(eskaera['From'],eskaera['Content'], Id)) #Datu basean eskaerako From, Content eta kontainerraren id-a gordeko dugu tupla batean
		cursor.execute("commit") #Aldaketak burutu
		return 0

@app.route("/test", methods=['GET']) #Test rutako eskaerak ALIVE testua bueltatuko digu, bere flask kontainerraren id-arekin batera
def test():
	return "ALIVE "+ socket.gethostname() #bueltatu alive eta kontainerraren id-a


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)

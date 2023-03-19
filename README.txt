Ezer baino lehen, honakoa egin Kontainer eta Networkak gelditu eta ezabatzeko:

> docker compose down

Zerbitzuak eraiki, sortu eta hasieratzeko honakoa erabili fitxategiak dauden tokian:

> docker compose build
> docker compose up

Exekutatzen ari dela, hona hemen proiektu honek dituen funtzionalitate desberdinak eta nola erabili hauek:

- http://ip/db motako eskaerak adminer kontainerrera joango dira

- http://ip/ motako URL-ak Flask replika multzora bidaliko dira. Hona hemen eskaintzen dituzten zerbitzuak:



-- GET /test : kontainer batek “ALIVE” textua bueltatzea espero da, kontainer beraren ID-arekin batera. Adibidez:

>curl localhost:80/test

ALIVE 14a6debcce33



-- POST /message : Eskaeraren edukia “mariadb” kontainerran dagoen datu basean gordeko du (JSON motakoa). Adibidez:

>curl -d '{"From":"norbait", "Content":"zerbait"}' -H "Content-Type: application/json" -X POST localhost:80/message

Gordeta

(Aurreko eskaera honek datu basean honako erregistroa sortuko luke {"norbait", "zerbait", <replikaren ID>-a})


-- GET /message : Datu basearen erregistroak bueltatuko ditu. Erregistroak Zeinek bidali dituen bidez filtratu daitezke.
		  Erregistro guztiak nahi badituzu From=ALL erabili:

>curl -X GET localhost:80/message?From=ALL

[["AAB","ttt","12a300031fa5"],["Ijurko","Andoni","d8738d985166"],["norbait","zerbait","14a6debcce33"]]


		  From jakin baten erregistroak nahi badituzu erabili honakoa (adibidez, From=norbait):


>curl -X GET localhost:80/message?From=norbait

[["norbait","zerbait","14a6debcce33"]]


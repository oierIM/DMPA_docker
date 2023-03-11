# Python 2.7 oinarri ofizial batetik abiatuko gara
FROM python
# kontainerra hasten denean, bere lan direktorioa honakoa izango da
WORKDIR /flaskProject
# Gure proiektuko fitxategi guztiak kontainerraren /app direktoriora kopiatuko ditugu:
# Uneko direktorioan dauzkagun fitxategiak kopiatuko dira, app.py eta requirements.txt
COPY . /flaskProject

#RUN apt-get update -y 

#RUN apt-get install -y libmariadb-dev

#docker search mariadb eta docker pull mariadb eginda terminaletik

#pip erabiliz, “requirements.txt” dauden menpekotasunak instalatuko ditugu.
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Kontainerra 80/tcp portutik komunikatuko dela adierazten dugu
EXPOSE 5000
# Ingurune aldagai bat sortuko dugu
ENV NAME World
# Kontainerra jaurtitzerakoan, honako komandoa exekutatuko da
CMD ["python", "app.py"]

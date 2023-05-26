from flask import render_template
from flask import Flask

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="NYC"
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/')
def unitList():
    mycursor.execute("SELECT * FROM NYC.Airbnb, NYC.neighborhood WHERE neighbourhood_group2=neighbourhood_group LIMIT 15")
    myresult=mycursor.fetchall()
    return render_template('nycairbnb.html', units=myresult)

@app.route('/<id>')
def id2539(id):
    mycursor.execute("SELECT * FROM NYC.Airbnb, NYC.neighborhood WHERE neighbourhood_group2=neighbourhood_group AND id= {} LIMIT 15 ".format(id))
    myresult=mycursor.fetchall()
    return render_template('id2539.html', myresult1=myresult)
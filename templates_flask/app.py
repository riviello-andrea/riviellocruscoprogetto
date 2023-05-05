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
    mycursor.execute("SELECT * FROM Airbnb limit 17")
    myresult=mycursor.fetchall()
    return render_template('nycairbnb.html', units=myresult)
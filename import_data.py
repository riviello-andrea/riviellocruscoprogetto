import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS NYC")

mycursor.execute("DROP TABLE IF EXISTS NYC.Airbnb")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS NYC.Airbnb (
    id INTEGER PRIMARY KEY,
    name TEXT,
    host_id INTEGER,
    host_name text,
    neighbourhood_group VARCHAR(30),
    neighbourhood VARCHAR(30),
    latitude VARCHAR(30),
    longitude VARCHAR(30),
    room_type VARCHAR(30),
    price VARCHAR(30),
    number_of_reviews INTEGER,
    last_review VARCHAR (30),
    reviews_per_month VARCHAR(10),
    calculated_host_listings_count INTEGER,
    availability_365 INTEGER
  );""")

mycursor.execute("DELETE FROM NYC.Airbnb")
mydb.commit()

clash_data = pd.read_csv('./AB_NYC_2019.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

print(len(clash_data.columns))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    sql = "INSERT INTO NYC.Airbnb VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM NYC.Airbnb")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
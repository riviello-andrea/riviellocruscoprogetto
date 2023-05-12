import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="NYC"
)
mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS NYC.neighborhood")

mycursor.execute("""
  CREATE TABLE IF NOT EXISTS NYC.neighborhood (
    neighbourhood_group2 VARCHAR(30),
    Borough VARCHAR(30),
    measurement INTEGER
  );""")

clash_data = pd.read_csv('./nyc_neighborhood.csv', index_col=False, delimiter = ',')
clash_data = clash_data.fillna('Null')
print(clash_data.head(20))

print(len(clash_data.columns))

#Fill the table
for i,row in clash_data.iterrows():
    cursor = mydb.cursor()
    sql = "INSERT INTO NYC.neighborhood VALUES (%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM NYC.neighborhood, NYC.Airbnb WHERE neighbourhood_group2=neighbourhood_group")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
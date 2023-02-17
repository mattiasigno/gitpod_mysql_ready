import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (Id VARCHAR(255), Nome_Proprio VARCHAR(255), Razza VARCHAR(255), Peso INT(255), Eta INT(255))")
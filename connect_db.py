import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= 'database_kontak'
  )

mycursor = mydb.cursor()
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="T3am10ftw!"
)


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS accounts")

mycursor.execute("""
USE accounts;
CREATE TABLE IF NOT EXISTS users (
    username varchar(255),
    password varchar(255)
);
""")

# TODO:  add the rest of the fields
# and also change the type of password to whatever our hash uses.


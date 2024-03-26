import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="T3am10ftw!"
)

mycursor = mydb.cursor()

option = input("""
                *** WARNING ***
Running this will delete everything in the database!
Only do this if you want to completely reset everything!
        Would you like continue? (y/n)
""")

if (option == "y"):
    try:
        mycursor.execute("DROP DATABASE accounts")
        print("'accounts' database deleted!")
    except:
        print("Something went wrong! Maybe the database doesn't exist on this machine?")

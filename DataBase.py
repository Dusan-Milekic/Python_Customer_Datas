import mysql.connector

#mysql connection creating
def OpenConnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SamoProgramiranjeNaMaks10!",
        database="sys"
    )
    return mydb


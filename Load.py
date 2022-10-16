#File to establish mysql connection, connect to database, and load in tables and data if needed

    #TODO compile data into csv and load it into respective table
import mysql.connector
import csv

import SqlCommands as command

mydb = mysql.connector.connect( # establish connection
    host="localhost",
    user="root",
    password='', #Edit password here to match user password
)

cursor = mydb.cursor()


#Check if database 'Basketball' exists
cursor.execute("DROP DATABASE Basketball")
cursor.execute("SHOW DATABASES") 

check = ""
for x in cursor:
    check += x[0];

#Create 'Basketball' if it doesn't exist and load tables and data into it
if 'Basketball' not in check:
    cursor.execute("CREATE DATABASE Basketball")
    cursor.execute("USE Basketball")

    cursor.execute( #Create Player table
    command.createPlayer
    )

    cursor.execute( #Create Season Stats table
    command.createSeason
    )

    cursor.execute( #Create Game Stats table
    command.createGame
    )

else: # Use 'Basketball' if it already exists
    cursor.execute("USE Basketball")


#Debug: Check if all tables are loaded in properly
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

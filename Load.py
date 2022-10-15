import mysql.connector


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

#Create 'Basketball' if it doesn't exist
if 'Basketball' not in check:
    cursor.execute("CREATE DATABASE Basketball")
    cursor.execute("USE Basketball")

    cursor.execute( #Create Player table
    """
    CREATE TABLE Player (
        id INT AUTO_INCREMENT, Year INT, Name VARCHAR(255), Team VARCHAR(255), 
        Age INT, Position VARCHAR(255), PRIMARY KEY (id, Year)
    )
    """
    )



else:
    cursor.execute("USE Basketball")




    











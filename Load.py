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

#Create 'Basketball' if it doesn't exist and load tables and data into it
if 'Basketball' not in check:
    cursor.execute("CREATE DATABASE Basketball")
    cursor.execute("USE Basketball")

    cursor.execute( #Create Player table
    """
    CREATE TABLE Player (
        id INT AUTO_INCREMENT, Year INT, Name VARCHAR(255), Team VARCHAR(255), 
        Age INT, Position VARCHAR(255), 
        PRIMARY KEY (id, Year)
    )
    """
    )

    cursor.execute( #Create Season Stats table
    """
    CREATE TABLE Season_stats (
        id INT AUTO_INCREMENT, Year INT, Games_played INT, Games_started INT, Minutes_played INT, Made_field_goals INT, 
        Attempted_field_goals INT, Made_3_pts INT, Attempted_3_pts INT, Made_ft INT, Attempted_ft INT, Offensive_rebounds INT,
        Defensive_rebounds INT, Assists INT, Steals INT, Blocks INT, Turnovers INT, Fouls INT, Points INT,
        PRIMARY KEY (id, Year)
    ) 
    """
    )

    





else: # Use 'Basketball' if it already exists
    cursor.execute("USE Basketball")

cursor.execute("SHOW TABLES")



    











#File to establish mysql connection, connect to database, and load in tables and data if needed

    #TODO compile data into csv and load it into respective table
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
        id VARCHAR(255), Year INT, Name VARCHAR(255), Team VARCHAR(255), 
        Age INT, Position VARCHAR(255), 
        PRIMARY KEY (id, Year)
    )
    """
    )

    cursor.execute( #Create Season Stats table
    """
    CREATE TABLE Season_stats (
        id VARCHAR(255), Year INT, Games_played INT, Games_started INT, Minutes_played INT, Made_field_goals INT, 
        Attempted_field_goals INT, Made_3_pts INT, Attempted_3_pts INT, Made_ft INT, Attempted_ft INT, Offensive_rebounds INT,
        Defensive_rebounds INT, Assists INT, Steals INT, Blocks INT, Turnovers INT, Fouls INT, Points INT,
        PRIMARY KEY (id, Year)
    ) 
    """
    )

    cursor.execute( #Create Game Stats table
    """
    CREATE TABLE Game_stats (
        id VARCHAR(255), Year INT, GameNum INT, Games_played INT, Outcome VARCHAR(255), Opponent VARCHAR(255), Team VARCHAR(255),
        Date VARCHAR(255), Location VARCHAR(255), Active VARCHAR(255), 
        Seconds_played INT,  Made_field_goals INT, Attempted_field_goals INT, Made_3_pts INT, Attempted_3_pts INT, 
        Made_ft INT, Attempted_ft INT, Offensive_rebounds INT, Defensive_rebounds INT, 
        Assists INT, Steals INT, Blocks INT, Turnovers INT, Fouls INT, Points INT, Game_score INT, Plus_minus INT,
        PRIMARY KEY (id, Year, GameNum)
    )
    
    """
    )

else: # Use 'Basketball' if it already exists
    cursor.execute("USE Basketball")


#Debug: Check if all tables are loaded in properly
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)



    











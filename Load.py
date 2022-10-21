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

    #Create tables
    cursor.execute( #Create Player table
    command.createPlayer
    )

    cursor.execute( #Create Season Stats table
    command.createSeason
    )

    cursor.execute( #Create Game Stats table
    command.createGame
    )

    for i in range(12,22): #Load season and player data
        year = int("20" + str(i))
        csvFile = "Data/" + str(year) + "_player_season_totals.csv"
        with open(csvFile, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != 'slug':
                    for x in range(len(row)):
                        row[x] = row[x].replace(" ", "_") #Replace Spaces for underscores for the values   
                    seasonRow = [row[0]]
                    seasonRow.append(year)
                    for x in range(5, len(row)):
                        seasonRow.append(int(row[x])) 
                    print(len(seasonRow))

                    
                    exeString  = """
                    INSERT INTO Season_stats(id, Year, Games_played, Games_started, Minutes_played, Made_field_goals, 
                    Attempted_field_goals, Made_3_pts, Attempted_3_pts, Made_ft, Attempted_ft, Offensive_rebounds, 
                    Defensive_rebounds, Assists, Steals, Blocks, Turnovers, Fouls, Points) 
                    VALUES(\"%s\", %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """ 
                    cursor.execute(exeString, seasonRow)
                    
                     
                   
                    cursor.execute(f"INSERT INTO Player(id, Year, Name, Team, Age, Position) VALUES(\"{row[0]}\", {year}, \"{row[1]}\", \"{row[4]}\", {int(row[3])}, \"{row[2]}\")")


            #Test if player data load
            cursor.execute("SELECT Name FROM Player WHERE Team=\"MEMPHIS_GRIZZLIES\" AND Year=2021")
            for x in cursor:
                print(x)       
         

    
    
            

else: # Use 'Basketball' if it already exists
    cursor.execute("USE Basketball")


#Debug: Check if all tables are loaded in properly
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

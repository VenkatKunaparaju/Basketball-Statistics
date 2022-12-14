import csv
createPlayer = """
    CREATE TABLE Player (
        id VARCHAR(255), Year INT, Name VARCHAR(255), Team VARCHAR(255), 
        Age INT, Position VARCHAR(255), 
        PRIMARY KEY (id, Year, Team)
    )
    """
createSeason =  """
    CREATE TABLE Season_stats (
        id VARCHAR(255), Year INT, Team VARCHAR(255), 
        Games_played INT, Games_started INT, Minutes_played INT, Made_field_goals INT, 
        Attempted_field_goals INT, Made_3_pts INT, Attempted_3_pts INT, Made_ft INT, Attempted_ft INT, Offensive_rebounds INT,
        Defensive_rebounds INT, Assists INT, Steals INT, Blocks INT, Turnovers INT, Fouls INT, Points INT,
        PRIMARY KEY (id, Year, Team)
    ) 
    """
createGame =   """
    CREATE TABLE Game_stats (
        id VARCHAR(255), Year INT, GameNum INT, Games_played INT, Outcome VARCHAR(255), Opponent VARCHAR(255), Team VARCHAR(255),
        Date VARCHAR(255), Location VARCHAR(255), Active VARCHAR(255), 
        Seconds_played INT,  Made_field_goals INT, Attempted_field_goals INT, Made_3_pts INT, Attempted_3_pts INT, 
        Made_ft INT, Attempted_ft INT, Offensive_rebounds INT, Defensive_rebounds INT, 
        Assists INT, Steals INT, Blocks INT, Turnovers INT, Fouls INT, Points INT, Game_score INT, Plus_minus INT,
        PRIMARY KEY (id, Year, GameNum)
    )
    
    """
seasonLoad  = """
                    INSERT INTO Season_stats(id, Year, Team, Games_played, Games_started, Minutes_played, Made_field_goals, 
                    Attempted_field_goals, Made_3_pts, Attempted_3_pts, Made_ft, Attempted_ft, Offensive_rebounds, 
                    Defensive_rebounds, Assists, Steals, Blocks, Turnovers, Fouls, Points) 
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """ 
playerLoad = """
                    INSERT INTO Player(id, Year, Name, Team, Age, Position) VALUES(%s, %s, %s, %s, %s, %s)
            """



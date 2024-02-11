import math

import psycopg2

hostname = 'localhost'
database = 'Task3Database'
username = 'postgres'
pwd = '0000'
port_id = 5433

def create_table():
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id
    )

    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS results(
                first_team VARCHAR (50) NOT NULL,
                second_team VARCHAR (50) NOT NULL,
                first_team_score int NOT NULL,
                second_team_score int NOT NULL,
                winner VARCHAR (50) NOT NULL);
                """)
    conn.commit()

    cur.close()
    conn.close()

def insert_table(data):
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id
    )
    cur = conn.cursor()

    insert_script = 'INSERT INTO results (first_team, second_team, first_team_score, second_team_score, winner) VALUES (%s,%s,%s,%s,%s)'
    insert_value = (data[0],data[1],data[2],data[3],data[4])
    cur.execute(insert_script,insert_value)

    conn.commit()
    cur.close()
    conn.close()

def fetch_data(team):
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id
    )
    cur = conn.cursor()
    fetch_script = 'SELECT * FROM results WHERE first_team = %s OR second_team = %s;'
    fetch_value = team
    cur.execute(fetch_script,(fetch_value,fetch_value))
    matches = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return matches

def calculate_points(first_team_matches, second_team_matches, first_team, second_team):
    first_team_point = 0
    second_team_point = 0
    first_team_count = 0
    second_team_count = 0

    for match in first_team_matches:
        if(match[0] == second_team or match[1] == second_team): # Birbirleri arasında oynamışlar ise
            if(match[4] == first_team):
                first_team_point = first_team_point + 6
                second_team_point = second_team_point - 1
            elif(match[4] == second_team):
                first_team_point = first_team_point - 1
                second_team_point = second_team_point + 6
            elif(match[4] == "Draw"):
                if(match[2] == 0 and match[3] == 0):
                    first_team_point = first_team_point + 1
                    second_team_point = second_team_point + 1
                else:
                    first_team_point = first_team_point + 2
                    second_team_point = second_team_point + 2
        elif(match[4] == first_team):
            first_team_point = first_team_point + 5
        elif(match[4] == "Draw"):
            if(match[2] == 0 and match[3] == 0):
                first_team_point = first_team_point + 1
            else:
                first_team_point = first_team_point + 2
        first_team_count = first_team_count + 1
                
    for match in second_team_matches:
        if(match[0] == first_team or match[1] == first_team): # Birbirleri arasında oynamışlar ama yukarıda düzenledik
            pass
        elif(match[4] == second_team):
            second_team_point = second_team_point + 5
        elif(match[4] == "Draw"):
            if(match[2] == 0 and match[3] == 0):
                second_team_point = second_team_point + 1
            else:
                second_team_point = second_team_point + 2
        second_team_count = second_team_count + 1
    
    first_team_average = round((first_team_point / first_team_count), 2)
    second_team_average = round((second_team_point / second_team_count), 2)

    return first_team_average,second_team_average

def find_posibility(first_avg, second_avg,first_team,second_team):
    if(first_avg > second_avg):
        a = first_avg
        b = second_avg
        winner = first_team
    else:
        a = second_avg
        b = first_avg
        winner = second_team

    temp = 1 + math.exp(-1 * (4 * (math.log(a + 1) - math.log(b + 1)) / math.log(6)))
    result = round(((1 / temp) * 100), 2)

    return winner,result

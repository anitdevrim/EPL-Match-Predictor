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

    insert_script = 'INSERT INTO results (first_team, second_team, first_team_score, second_team_score,winner) VALUES (%s,%s,%s,%s,%s)'
    insert_value = (data[0],data[1],data[2],data[3],data[4])
    cur.execute(insert_script,insert_value)

    conn.commit()
    cur.close()
    conn.close()

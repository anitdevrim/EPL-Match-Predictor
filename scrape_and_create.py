from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By

from funcs import create_table, insert_table

create_table()

start_date =  datetime(2024, 1, 20)
end_date= datetime(2024, 2 , 5)
step = timedelta(days=1)
current_date = start_date

driver = webdriver.Chrome()

while current_date <= end_date:
    date_for_url = current_date.strftime('%Y%m%d')
    driver.get(f'https://www.espn.com/soccer/scoreboard/_/date/{date_for_url}/league/eng.1')

    matches = driver.find_elements(By.CLASS_NAME, 'Scoreboard')

    for match in matches:
        team = match.find_elements(By.CLASS_NAME, 'ScoreCell__TeamName')
        score = match.find_elements(By.CLASS_NAME, 'ScoreCell__Score')
        
        if(int(score[0].text) > int(score[1].text)):
            winner = team[0].text
        elif(int(score[0].text) < int(score[1].text)):
            winner = team[1].text
        else:
            winner = "Draw"
        
        temp = [team[0].text, team[1].text, int(score[0].text), int(score[1].text), winner]
        insert_table(temp)
        

    current_date = current_date + step

from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By

start_date =  datetime(2024, 1, 29)
end_date= datetime(2024, 2 ,5)
step = timedelta(days=1)
current_date = start_date

driver = webdriver.Chrome()
results = []

while current_date <= end_date:
    date_for_url = current_date.strftime('%Y%m%d')
    driver.get(f'https://www.espn.com/soccer/scoreboard/_/date/{date_for_url}/league/eng.1')

    matches = driver.find_elements(By.CLASS_NAME, 'Scoreboard')

    for match in matches:
        team = match.find_elements(By.CLASS_NAME, 'ScoreCell__TeamName')
        score = match.find_elements(By.CLASS_NAME, 'ScoreCell__Score')
        temp = [team[0].text, team[1].text, int(score[0].text), int(score[1].text)]
        results.append(temp)

    current_date = current_date + step

for i in results:
    print(i)

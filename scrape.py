from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By

start_date =  datetime(2024, 1, 1)
end_date= datetime(2024, 2 ,5)
step = timedelta(days=1)

driver = webdriver.Chrome()


driver.get("https://www.espn.com/soccer/scoreboard/_/date/20240130/league/eng.1")

matches = driver.find_elements(By.CLASS_NAME, 'Scoreboard')

results = []

for match in matches:
    team = match.find_elements(By.CLASS_NAME, 'ScoreCell__TeamName')
    score = match.find_elements(By.CLASS_NAME, 'ScoreCell__Score')
    temp = [team[0].text, team[1].text, int(score[0].text), int(score[1].text)]
    results.append(temp)

print(results)
print(start_date)


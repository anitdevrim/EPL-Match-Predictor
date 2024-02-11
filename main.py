
from funcs import calculate_points, fetch_data

first_team = input("Enter the first team:\n").capitalize()
second_team = input("Enter the second team:\n").capitalize()

first_team_matches = fetch_data(first_team)
second_team_matches = fetch_data(second_team)

points = calculate_points(first_team_matches,second_team_matches,first_team, second_team)

print(points)

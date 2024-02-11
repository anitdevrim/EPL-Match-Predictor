
from funcs import calculate_points, fetch_data, find_posibility

first_team = input("Enter the first team:\n").title()
second_team = input("Enter the second team:\n").title()

first_team_matches = fetch_data(first_team)
second_team_matches = fetch_data(second_team)

points = calculate_points(first_team_matches,second_team_matches,first_team, second_team)

result = find_posibility(points[0],points[1],first_team, second_team)

print(f"The possibility of {result[0]} to win is {result[1]}")

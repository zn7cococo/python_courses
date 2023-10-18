list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

numbers = len(list_players)//2
team1 = list_players[:numbers]
team2 = list_players[numbers:]
print(team1)
print(team2)

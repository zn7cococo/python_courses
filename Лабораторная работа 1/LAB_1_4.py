users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

my_dict = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
my_dict["Общее количество"] += len(users)
my_dict["Уникальные посещения"] += len(set(users))

print(my_dict)
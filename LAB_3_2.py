def find_common_participants(participants_first_group, participants_second_group, splitter = ','):
    first_set = set(str.split(participants_first_group,splitter))
    second_set = set(str.split(participants_second_group,splitter))
    return list(first_set.intersection(second_set))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group, splitter = '|'))

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2 # выбор центрального элемента
first_team = list_players[:middle_index]  # разбивка до центрального элемента без включения
second_team = list_players[middle_index:]  # разбивка после центрального элемента с включением
print(first_team)
print(second_team)


numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
none_number = 4  # номер пропущенного элемента
sum_numbers = sum(numbers[:none_number]) + sum(numbers[none_number+1:])  # подсчет суммы без пропущенного номера
len_numbers = len(numbers)  # подсчет количества чисел
numbers[none_number] = sum_numbers/len_numbers  # замена пропущенного номера
print("Измененный список:", numbers)



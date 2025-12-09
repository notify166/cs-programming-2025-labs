# Задание 1


numbers = [1, 5, 8, 3, 12, 100, 7, 15, 20, 6]
target = 3
repnum = 30
if target in numbers:
    index = numbers.index(target)
    numbers[index] = replacement_number
    print(f"Обновленный список: {numbers}")
else:
    print(f"Число {target_number} не найдено в списке.")
# Задание 1


numbers = [1, 5, 8, 3, 12, 100, 7, 15, 20, 6]
target = 3
repnum = 30
if target in numbers:
    index = numbers.index(target)
    numbers[index] = repnum
    print(f"Обновленный список: {numbers}")
else:
    print(f"Число {target} не найдено в списке.")


# Задание 2

nums = [4, 11, 22, 33]
sq = []
for num in nums:
    sq.append(num ** 2)
print(sq)


# Задание 3
numbrs = [4, 42, 16, 11, 22, 14]
maxx = max(numbrs)
lg = len(numbrs)
print(maxx/lg)

# Задание 4

d = (3, 1, 4, 7)
dcheck = all(isinstance(x, (int, float)) for x in d)
if dcheck:
    sorted_d = tuple(sorted(d))
else:
    sorted_d = d
print(sorted_d)


# Задание 5

products = {"яблоко": 50, "банан": 30, "ананас": 120, "груша": 45}

print(min(products, key=products.get))
print(max(products, key=products.get))


# Задание 6
lst = ["apple", 5, True]

result = {item: item for item in lst}
print(result)



# Задание 7
words = {
    "cat": "кот",
    "dog": "собака",
    "apple": "яблоко"
}

rus_word = input("Введите слово: ")

reverse_dict = {v: k for k, v in words.items()}

print(reverse_dict.get(rus_word, "Слова нет в словаре"))

# Задание 8
import random

choices = ["камень", "ножницы", "бумага", "ящерица", "спок"]

wins = {
    "ножницы": {"бумага", "ящерица"},
    "бумага": {"камень", "спок"},
    "камень": {"ножницы", "ящерица"},
    "ящерица": {"спок", "бумага"},
    "спок": {"ножницы", "камень"}
}

user = input(f"Выбери {choices}: ").lower()
bot = random.choice(choices)

print("Ты:", user)
print("Компьютер:", bot)

if user == bot:
    print("Ничья")
elif user in wins and bot in wins[user]:
    print("Ты победил!")
else:
    print("Победил компьютер!")


# Задание 9

words = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]

result = {}
for w in words:
    key = w[0]
    result.setdefault(key, []).append(w)

print(result)

# Задание 10
students = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]

avg = {name: sum(marks) / len(marks) for name, marks in students}

best_name = max(avg, key=avg.get)
print(f"{best_name} имеет наивысший средний балл: {avg[best_name]:.1f}")



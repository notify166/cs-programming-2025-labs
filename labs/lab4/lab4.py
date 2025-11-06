temp = int(input('Введите текущую температуру в комнате: '))
if temp > 19:
    print('Кондиционер выключен')
else:
    print('Кондиционер включен')

# Задание 1



num_month = int(input('Введите текущий месяц: '))
if num_month == 1 or num_month == 2 or num_month == 12:
    print('Сейчас зима')
elif num_month == 3 or num_month == 4 or num_month == 5:
    print('Сейчас весна')
elif num_month == 6 or num_month == 7 or num_month == 8:
    print('Сейчас лето')
elif num_month == 9 or num_month == 10 or num_month == 11:
    print('Сейчас осень')


# Задание 2



age = float(input('Введите возраст собаки: '))
human_age = 0
if age <= 0:
    print('Ошибка. Возраст собаки должен быть больше 0!')
elif age > 22:
    print('Ошибка. Возраст собаки должен быть меньше 22!')
else:
    if age <= 2:
        human_age = age * 10.5
    else:
        human_age = 21 + (age - 2) * 4
print(f'Вашей собаке {human_age} лет в человеческих годах')

# Задание 3
        


number = int(input('Введите число: '))
str_num = str(number)
def summ(n):
    return sum(map(int,str(n)))
if int(str_num[-1]) % 2 == 0 and summ(number) % 3 == 0:
    print(number / 6)
else:
    print('Ваше число не прошло условие')


# Задание 4



password = input("Введите пароль: ")
errors = []

if len(password) < 8:
    errors.append("длина менее 8 символов")
if not any(c.isupper() for c in password):
    errors.append("отсутствуют заглавные буквы")
if not any(c.islower() for c in password):
    errors.append("отсутствуют строчные буквы")
if not any(c.isdigit() for c in password):
    errors.append("отсутствуют числа")
if password.isalnum():
    errors.append("отсутствуют специальные символы")

print("Пароль ненадежный: " + ", ".join(errors) if errors else "Пароль надежный!")


# Задание 5



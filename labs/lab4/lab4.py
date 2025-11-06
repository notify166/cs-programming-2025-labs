from types import ModuleType


temp = int(input('Введите температуру: '))
if temp >= 20:
    print('Кондиционер выключен')
else:
    print('Кондиционер включен') # Задание 1


month = int(input('Введите номер месяца: '))
if month == 1 or month == 2 or month == 12:
    print('Сейчас зима')     
elif month == 3 or month == 4 or month == 5:
    print('Сейчас весна')     
elif month == 6 or month == 7 or month == 8:
    print('Сейчас лето')     
elif month == 9 or month == 10 or month == 11:
    print('Сейчас осень')                          #Задание 2



#dogage = int(input('Введите возраст собаки: '))
#if dogage > 22:
#    print('Ошибка: возраст должен быть не больше 22')
#    if dogage < 1:
#        print('Ошибка: возраст должен быть не меньше 1')
#
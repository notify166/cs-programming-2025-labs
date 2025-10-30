name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
for i in range(10):
    print(f"Меня зовут {name}, мне {age} лет") # Задание 1


n = input("Введите число от 1 до 9: ")
b = 1
if int(n) > 0 and int(n) < 10:
    while b < 10:
        print(int(n)*b)
        b+=1
else:
    print("Ваше число не подходит")  # Задание 2



n = 1
while n < 101:
    if n%3==0:
        print(n)
        n+=1
    else:
        n+=1  # Задание 3

from math import *

number = int(input("Введите число: "))
print(factorial(number))   Задание 4

a = 20
while a != -1:
   print(a)
    a = a-1 # Задание 5

number1 = int(input("Введите число:"))
a = 0
b = 1
c = 0
while c<number1:
    c = a + b
   print(c)
    a = b
    b = c  # Задание 6

word = input('Введите слово: ')
answer = []
f = 1
for letter in word:
    mas.append(letter)
    mas.append(str(f))
    f += 1
print(*answer, sep='') #Задание 7

while True:
    a, b = input('Введите два числа через пробел: ').split()
    print('Сумма равна = ', int(a) + int(b)) #Задание 8
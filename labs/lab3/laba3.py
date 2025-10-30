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



s = 1
while s < 101:
    if s%3==0:
        print(s)
        s+=1
    else:
        s+=1  # Задание 3

fact = int(input('Введите число: '))
ans = 1
for i in range (1, fact+1):
    ans = ans * i
print(ans)


Z = 20
while Z != -1:
   print(Z)
   Z = Z-1 # Задание 5

number1 = int(input("Введите число:"))
a = 0
b = 1
c = 0
print(a)
print(b)
while c<number1:
    c = a + b
    if c > number1:
        break
    else:
        a = b
        b = c
        print(c)  # Задание 6

word = input('Введите слово: ')
answer = []
f = 1
for letter in word:
    answer.append(letter)
    answer.append(str(f))
    f += 1
print(*answer, sep='') #Задание 7

while True:
    a, b = input('Введите два числа через пробел: ').split()
    print('Сумма равна = ', int(a) + int(b)) #Задание 8
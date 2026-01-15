# Задание 1
def convert(value, frm, to):
    sec = {"s": 1, "m": 60, "h": 3600}
    return value * sec[frm] / sec[to]

print(convert(4, "h", "m"), "m")
# Задание 2
def profit(a, n):
    if a < 30000:
        return "Error!"
    add = min((a // 10000) * 0.3, 5)
    if n <= 3: rate = 3
    elif n <= 6: rate = 5
    else: rate = 2
    rate = (rate + add) / 100
    total = a
    for _ in range(n):
        total += total * rate
    return round(total - a, 2)

print(profit(40000, 8))
# Задание 3
def primes(a, b):
    if a > b or b < 2:
        return "Error!"
    res = []
    for x in range(max(2, a), b + 1):
        if all(x % i for i in range(2, int(x**0.5) + 1)):
            res.append(x)
    return res if res else "Error!"

print(primes(1, 10))
# Задание 4
def add_matrix(a, b):
    n = len(a)
    if n <= 2 or n != len(b):
        return "Error!"
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]

m1 = [[2, 5, 1], [5, 3, 2], [1, 1, 1]]
m2 = [[5, 2, 4], [4, 1, 3], [2, 2, 2]]

print(add_matrix(m1, m2))
# Задание 5
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return "Да" if s == s[::-1] else "Нет"

print(is_palindrome("А роза упала на лапу Азора"))

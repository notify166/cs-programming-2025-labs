# Задание 1
objects = [
    ("Z", 4),
    ("V", 1),
    ("O", 3),
    ("S", 2)
]

print(sorted(objects, key=lambda x: x[1]))
# Задание 2
staff_shifts = [
    {"name": "Кристина", "shift_cost": 120, "shifts": 15},
    {"name": "Влад", "shift_cost": 90, "shifts": 22},
    {"name": "Михаил", "shift_cost": 150, "shifts": 10}
]

costs = list(map(lambda x: x["shift_cost"] * x["shifts"], staff_shifts))
print(costs)
print(max(costs))
# Задание 3
personnel = [
    {"name": "Михаил", "lv": 2},
    {"name": "Даниил", "lv": 4},
    {"name": "Илья", "lv": 1}
]

result = list(map(lambda p: {
    **p,
    "category": "Лаборант" if p["lv"] == 1 else
                "Доктор Наук" if p["lv"] <= 3 else
                "О5"
}, personnel))

print(result)
# Задание 4
zones = [
    {"zone": "Zone1", "active_from": 8, "active_to": 18},
    {"zone": "Zone2", "active_from": 0, "active_to": 24},
    {"zone": "Zone3", "active_from": 9, "active_to": 17}
]

print(list(filter(lambda z: z["active_from"] >= 8 and z["active_to"] <= 18, zones)))
# Задание 5
отчеты = [
    {"автор": "Доктор Мосс", "текст": "Анализ завершён. Ссылка: http://архив.нет"},
    {"автор": "Агент Ли", "текст": "Инцидент устранён."},
    {"автор": "Доктор Патель", "текст": "Данные доступны по адресу https://исследования.орг"}
]

с_ссылками = filter(lambda r: "http" in r["текст"], отчеты)

очищенные = list(map(lambda r: {
    "автор": r["автор"],
    "текст": "[ДАННЫЕ УДАЛЕНЫ]"
}, с_ссылками))

print(очищенные)
# Задание 6
объекты_scp = [
    {"scp": "SCP-096", "класс": "Евклид"},
    {"scp": "SCP-173", "класс": "Евклид"},
    {"scp": "SCP-055", "класс": "Кетер"},
    {"scp": "SCP-999", "класс": "Безопасный"}
]

print(list(filter(lambda o: o["класс"] != "Безопасный", объекты_scp)))
# Задание 7
инциденты = [
    {"id": 101, "персонал": 4},
    {"id": 102, "персонал": 12},
    {"id": 103, "персонал": 7},
    {"id": 104, "персонал": 20}
]

print(sorted(инциденты, key=lambda x: x["персонал"], reverse=True)[:3])
# Задание 8
протоколы = [
    ("Блокировка", 5),
    ("Эвакуация", 4),
    ("Очистка данных", 3),
    ("Плановая проверка", 1)
]

print(list(map(lambda p: f"Протокол {p[0]} — уровень критичности {p[1]}", протоколы)))
# Задание 9
смены = [6, 12, 8, 24, 10, 4]

print(list(filter(lambda s: 8 <= s <= 12, смены)))
# Задание 10
оценки = [
    {"имя": "Кирилл", "балл": 78},
    {"имя": "Вайс", "балл": 92},
    {"имя": "Артем", "балл": 61},
    {"имя": "Леха", "балл": 88}
]

лучший = max(оценки, key=lambda x: x["балл"])
print(лучший["имя"], лучший["балл"])


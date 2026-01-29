#!/usr/bin/env python3
# rpg_v2.py — RPG с обновленной системой инвентаря
import random, sys

##### 1. Конфигурация и константы
MAX_INVENTORY_SLOTS = 5

RACES = {
    "1": ("Человек", {"HP": (70, 90), "ATK": (8, 12), "DEF": (4, 8), "AGI": (6, 10)}),
    "2": ("Эльф", {"HP": (60, 80), "ATK": (6, 10), "DEF": (3, 6), "AGI": (10, 14)}),
    "3": ("Дворф", {"HP": (80, 100), "ATK": (9, 13), "DEF": (6, 10), "AGI": (4, 8)})
}


##### 2. Классы
class Character:
    def __init__(self, name, race_key):
        self.name = name
        self.race_key = race_key
        self.race = RACES[race_key][0]
        # Характеристики
        vals = RACES[race_key][1]
        self.max_hp = random.randint(*vals["HP"])
        self.hp = self.max_hp
        self.atk = random.randint(*vals["ATK"])
        self.defn = random.randint(*vals["DEF"])
        self.agi = random.randint(*vals["AGI"])
        # Прогресс
        self.level = 1
        self.xp = 0
        self.next_xp = 10
        self.free_points = 0
        # Экипировка (активная)
        self.weapon = None
        self.armor = None
        # Инвентарь (список объектов) и золото
        self.inventory = []
        self.gold = 0

        # Стартовый набор: 2 зелья
        self.add_item_force({"name": "Малое зелье", "type": "potion", "val": 30})
        self.add_item_force({"name": "Малое зелье", "type": "potion", "val": 30})

    def effective_atk(self):
        w_atk = self.weapon["val"] if self.weapon else 0
        return self.atk + w_atk

    def effective_def(self):
        a_def = self.armor["val"] if self.armor else 0
        return self.defn + a_def

    # Добавление предмета без проверок (для старта)
    def add_item_force(self, item):
        if len(self.inventory) < MAX_INVENTORY_SLOTS:
            self.inventory.append(item)

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.next_xp:
            self.xp -= self.next_xp
            self.level += 1
            self.free_points += 3
            self.next_xp = int(self.next_xp * 1.5)
            print(f"\n*** Поздравляем — уровень {self.level}! Получено 3 очка прокачки. ***")


class Enemy:
    def __init__(self, floor=1):
        base = 5 + floor
        self.hp = random.randint(base * 4, base * 6)
        self.atk = random.randint(base, base + 3)
        self.defn = random.randint(base // 2, base)
        self.agi = random.randint(3, 6)
        self.name = random.choice(["Скелет", "Гоблин", "Крыс", "Тёмный воин"])


class ItemGenerator:
    @staticmethod
    def potion(floor=1):
        # Сила зелья растет немного с этажами
        val = 30 + (floor * 5)
        return {"name": f"Зелье ({val}hp)", "type": "potion", "val": val}

    @staticmethod
    def weapon(floor=1):
        return {"name": f"Меч+{floor}", "type": "weapon", "val": floor}

    @staticmethod
    def armor(floor=1):
        return {"name": f"Доспех+{floor}", "type": "armor", "val": floor}


##### 3. Логика инвентаря (Функции управления)

def add_item_to_inventory(player: Character, item):
    """
    Пытается добавить предмет. Если места нет — диалог замены.
    """
    print(f"\nПолучен предмет: {item['name']}")

    if len(player.inventory) < MAX_INVENTORY_SLOTS:
        player.inventory.append(item)
        print("Предмет добавлен в инвентарь.")
    else:
        print(f"!!! Инвентарь полон ({len(player.inventory)}/{MAX_INVENTORY_SLOTS}) !!!")
        print("Хотите выбросить что-то из сумки, чтобы взять новый предмет?")
        print("(n) - Нет, оставить старое")

        # Показываем список для выбора
        for idx, inv_item in enumerate(player.inventory):
            print(f"({idx + 1}) {inv_item['name']}")

        choice = input("> ").strip().lower()
        if choice == 'n':
            print(f"Вы оставили {item['name']} на земле.")
            return

        # Попытка замены
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(player.inventory):
                removed = player.inventory[idx]
                player.inventory[idx] = item
                print(f"Вы выбросили {removed['name']} и взяли {item['name']}.")
            else:
                print("Неверный номер. Предмет потерян.")
        except ValueError:
            print("Ошибка ввода. Предмет потерян.")


def open_inventory_menu(player: Character):
    """
    Меню просмотра и использования предметов вне боя
    """
    while True:
        print(f"\n--- ИНВЕНТАРЬ ({len(player.inventory)}/{MAX_INVENTORY_SLOTS}) ---")
        if not player.inventory:
            print("Пусто.")
        else:
            for i, item in enumerate(player.inventory):
                tag = ""
                if item['type'] == 'potion':
                    tag = "[Лечение]"
                elif item['type'] == 'weapon':
                    tag = "[Оружие]"
                elif item['type'] == 'armor':
                    tag = "[Броня]"
                print(f"{i + 1}. {item['name']} {tag}")

        print("\n(номер) Использовать/Экипировать  (d + номер) Выбросить  (q) Назад")
        cmd = input("> ").strip().lower()

        if cmd == 'q':
            break

        # Логика выбрасывания (d1, d2...)
        if cmd.startswith('d'):
            try:
                idx = int(cmd[1:]) - 1
                if 0 <= idx < len(player.inventory):
                    removed = player.inventory.pop(idx)
                    print(f"Вы выбросили {removed['name']}.")
                else:
                    print("Неверный слот.")
            except:
                print("Ошибка.")
            continue

        # Логика использования
        try:
            idx = int(cmd) - 1
            if 0 <= idx < len(player.inventory):
                item = player.inventory[idx]

                if item['type'] == 'potion':
                    heal_amount = item['val']
                    if player.hp >= player.max_hp:
                        print("Здоровье и так полное!")
                    else:
                        old_hp = player.hp
                        player.hp = min(player.max_hp, player.hp + heal_amount)
                        print(f"Выпито {item['name']}. HP: {old_hp} -> {player.hp}")
                        player.inventory.pop(idx)  # Удаляем использованное зелье

                elif item['type'] == 'weapon':
                    # Смена оружия
                    old_w = player.weapon
                    player.weapon = item
                    print(f"Вы взяли в руки {item['name']}.")
                    player.inventory.pop(idx)
                    if old_w:
                        # Возвращаем старое оружие в инвентарь (место только что освободилось)
                        player.inventory.insert(idx, old_w)
                        print(f"{old_w['name']} убран в рюкзак.")

                elif item['type'] == 'armor':
                    # Смена брони
                    old_a = player.armor
                    player.armor = item
                    print(f"Вы надели {item['name']}.")
                    player.inventory.pop(idx)
                    if old_a:
                        player.inventory.insert(idx, old_a)
                        print(f"{old_a['name']} убран в рюкзак.")
            else:
                print("Неверный слот.")
        except ValueError:
            print("Неверная команда.")


##### 4. Боевой цикл
def combat(player: Character, enemy: Enemy):
    print(f"\n!!! БОЙ !!! {enemy.name} (HP:{enemy.hp} ATK:{enemy.atk})")

    while enemy.hp > 0 and player.hp > 0:
        # Считаем зелья для отображения
        potions_count = sum(1 for i in player.inventory if i['type'] == 'potion')

        print(f"\nHP: {player.hp}/{player.max_hp} | Зелий в сумке: {potions_count}")
        print("(1) Атаковать  (2) Зелье (авто)  (3) Побег")

        cmd = input("> ").strip()

        if cmd == "1":
            dmg = max(1, player.effective_atk() - enemy.defn // 2)
            if random.random() < player.agi / 100:
                dmg = int(dmg * 1.5);
                print("КРИТИЧЕСКИЙ УДАР! ", end="")
            enemy.hp -= dmg
            print(f"Вы нанесли {dmg} урона. Враг: {max(enemy.hp, 0)} HP")

        elif cmd == "2":
            # Ищем первое попавшееся зелье
            potion_idx = -1
            for i, item in enumerate(player.inventory):
                if item['type'] == 'potion':
                    potion_idx = i
                    break

            if potion_idx != -1:
                pot = player.inventory[potion_idx]
                heal = pot['val']
                player.hp = min(player.max_hp, player.hp + heal)
                print(f"Вы использовали {pot['name']}, восстановлено {heal} HP.")
                player.inventory.pop(potion_idx)  # Удаляем конкретное зелье (слот)
            else:
                print("У вас нет зелий в инвентаре!")
                continue  # Ход не тратится, если нет зелья

        elif cmd == "3":
            if random.random() < 0.5 + player.agi / 100:
                print("Вы успешно сбежали!")
                return False
            print("Побег не удался.")
        else:
            print("Неверная команда.")
            continue

        # Ответ врага
        if enemy.hp > 0:
            edmg = max(1, enemy.atk - player.effective_def() // 2)
            if random.random() < enemy.agi / 100:
                edmg = int(edmg * 1.3)
            player.hp -= edmg
            print(f"{enemy.name} атакует на {edmg} урона! У вас {max(player.hp, 0)} HP.")

    if player.hp <= 0:
        print("\nВас убили... Игра окончена.")
        sys.exit(0)

    # Победа
    xp = random.randint(5, 10)
    g = random.randint(1, 5)
    player.gain_xp(xp)
    player.gold += g
    print(f"Победа! Получено {xp} XP и {g} золота.")

    # Дроп
    if random.random() < 0.4:
        # Может выпасть зелье или экипировка
        r = random.random()
        if r < 0.5:
            drop = ItemGenerator.potion(floor=1)  # Упрощено для примера
        elif r < 0.75:
            drop = ItemGenerator.weapon(floor=1)
        else:
            drop = ItemGenerator.armor(floor=1)

        add_item_to_inventory(player, drop)

    return True


##### 5. Генерация и исследование
def gen_room_type(floor):
    r = random.random()
    if r < 0.55: return "battle"
    if r < 0.8: return "rest"
    return "chest"


def explore(player: Character, floor=1):
    rooms_passed = 0
    while True:
        left = gen_room_type(floor)
        right = gen_room_type(floor)

        # Видимость
        visible = random.random() < 0.5
        print(f"\n--- Этаж {floor} | Комната {rooms_passed + 1} ---")
        if visible:
            print(f"Слева: {translate_room(left)} | Справа: {translate_room(right)}")
        else:
            print("Слева: ??? | Справа: ???")

        print("(1) Налево  (2) Направо  (i) Инвентарь  (s) Статус  (q) Выход")
        choice = input("> ").strip().lower()

        if choice == "i":
            open_inventory_menu(player)
            continue
        if choice == "s":
            show_status(player)
            continue
        if choice == "q":
            print("Вы покидаете подземелье. До встречи!")
            break

        room = left if choice == "1" else right if choice == "2" else None
        if room is None:
            print("Неверный выбор.");
            continue

        # Обработка комнаты
        if room == "battle":
            enemy = Enemy(floor)
            combat(player, enemy)

        elif room == "rest":
            heal = max(1, int(player.max_hp * 0.2))
            player.hp = min(player.max_hp, player.hp + heal)
            print(f"\nЛагерь. Вы перевязали раны (+{heal} HP).")
            if player.free_points:
                auto_allocate(player)

        else:  # chest
            g_amount = random.randint(3, 8)
            player.gold += g_amount
            print(f"\nСундук! Вы нашли {g_amount} монет.")

            # Шанс найти предмет в сундуке
            if random.random() < 0.6:
                # 50% зелье, 50% вещь
                if random.random() < 0.5:
                    item = ItemGenerator.potion(floor)
                else:
                    item = ItemGenerator.random_armor(floor) if random.random() < 0.5 else ItemGenerator.random_weapon(
                        floor)

                # Добавляем через нашу новую умную функцию
                add_item_to_inventory(player, item)

        rooms_passed += 1
        if rooms_passed % 5 == 0:
            floor += 1
            print(f"\n>>> Вы спускаетесь глубже... Этаж {floor} >>>")


def translate_room(rtype):
    if rtype == "battle": return "Враг"
    if rtype == "rest": return "Отдых"
    if rtype == "chest": return "Сундук"
    return rtype


##### 6. Утилиты
def show_status(p: Character):
    w_name = p.weapon['name'] if p.weapon else "Кулаки"
    a_name = p.armor['name'] if p.armor else "Тряпки"

    print(f"\n=== {p.name} ({p.race}) L{p.level} ===")
    print(f"XP: {p.xp}/{p.next_xp} | Золото: {p.gold}")
    print(f"HP: {p.hp}/{p.max_hp}")
    print(f"ATK: {p.atk} (+{p.weapon['val'] if p.weapon else 0}) [{w_name}]")
    print(f"DEF: {p.defn} (+{p.armor['val'] if p.armor else 0}) [{a_name}]")
    print(f"AGI: {p.agi}")
    print(f"Инвентарь: {len(p.inventory)}/{MAX_INVENTORY_SLOTS} слотов занято")


def auto_allocate(p: Character):
    print(f"У вас {p.free_points} очков прокачки. Распределить? (y/n)")
    if input("> ").strip().lower().startswith("y"):
        while p.free_points > 0:
            print(f"Осталось {p.free_points}. (1) HP+5 (2) ATK+1 (3) DEF+1 (4) AGI+1")
            c = input("> ").strip()
            if c == "1":
                p.max_hp += 5; p.hp += 5
            elif c == "2":
                p.atk += 1
            elif c == "3":
                p.defn += 1
            elif c == "4":
                p.agi += 1
            else:
                continue
            p.free_points -= 1
        print("Готово.")


##### 7. Старт
def create_character():
    print("Выберите расу:")
    for k, v in RACES.items(): print(f"{k} - {v[0]}")
    while True:
        r = input("> ").strip()
        if r in RACES:
            name = input("Имя героя: ").strip() or "Безымянный"
            p = Character(name, r)
            print("\nГерой создан!")
            show_status(p)
            return p
        print("Нет такой расы.")


def main():
    print("=== Текстовая RPG  ===")
    p = create_character()
    print("\nВы входите в подземелье...")
    explore(p)


if __name__ == "__main__":
    main()
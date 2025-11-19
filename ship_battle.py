import random

SIZE = 10
SHIP = "[#]"
HIT = "[%]"
MISS = "[@]"
EMPTY = "[_]"

def create_pole():
    pole = []
    for _ in range(SIZE):
        row = []
        for _ in range(SIZE):
            row.append(EMPTY)
        pole.append(row)
    return pole

def show_pole(pole):
    print()
    for i in range(SIZE):
        for j in range(SIZE):
            print(pole[i][j], end=" ")
        print()
    print()

def show_pole_masked(pole):
    print()
    for i in range(SIZE):
        for j in range(SIZE):
            cell = pole[i][j]
            if cell == SHIP:
                print(EMPTY, end=" ")
            else:
                print(cell, end=" ")
        print()
    print()

def around_cells(i, j):
    cells = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < SIZE and 0 <= y < SIZE:
                cells.append((x, y))
    return cells

def can_place_ship(pole, i, j):
    if pole[i][j] != EMPTY:
        return False
    for x, y in around_cells(i, j):
        if pole[x][y] == SHIP:
            return False
    return True

def place_single_ships(pole, count):
    placed = 0
    while placed < count:
        i = random.randint(0, SIZE - 1)
        j = random.randint(0, SIZE - 1)
        if can_place_ship(pole, i, j):
            pole[i][j] = SHIP
            placed += 1

def count_ships(pole):
    total = 0
    for row in pole:
        total += row.count(SHIP)
    return total

def user_turn(pole_enemy):
    while True:
        i = int(input("Введи i (0-9): "))
        j = int(input("Введи j (0-9): "))
        if i < 0 or i >= SIZE or j < 0 or j >= SIZE:
            print("Нет такой клетки.")
            continue
        cell = pole_enemy[i][j]
        if cell == HIT or cell == MISS:
            print("Ты уже стрелял сюда.")
            continue
        if cell == SHIP:
            pole_enemy[i][j] = HIT
            print("Попадание.")
            return True
        if cell == EMPTY:
            pole_enemy[i][j] = MISS
            print("Мимо.")
            return False

def bot_turn(pole_user):
    while True:
        i = random.randint(0, SIZE - 1)
        j = random.randint(0, SIZE - 1)
        cell = pole_user[i][j]
        if cell == HIT or cell == MISS:
            continue
        if cell == SHIP:
            pole_user[i][j] = HIT
            print("Бот попал в", i, j)
            return True
        if cell == EMPTY:
            pole_user[i][j] = MISS
            print("Бот промахнулся в", i, j)
            return False

def save_stats(winner, moves):
    with open("stats.txt", "a") as f:
        f.write(winner + " " + str(moves) + "\n")

def game():
    user_pole = create_pole()
    bot_pole = create_pole()

    place_single_ships(user_pole, 4)
    place_single_ships(bot_pole, 4)

    moves = 0

    while True:
        moves += 1

        print("Твоё поле:")
        show_pole(user_pole)
        print("Поле бота:")
        show_pole_masked(bot_pole)

        user_turn(bot_pole)
        if count_ships(bot_pole) == 0:
            print("Ты победил.")
            save_stats("user", moves)
            break

        bot_turn(user_pole)
        if count_ships(user_pole) == 0:
            print("Бот победил.")
            save_stats("bot", moves)
            break

game()

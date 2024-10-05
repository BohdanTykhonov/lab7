teams = {
    "Динамо": 42,
    "Шахтар": 48,
    "Металіст": 36,
    "Зоря": 44,
    "Десна": 39,
    "Львів": 35,
    "Олександрія": 33,
    "Ворскла": 30,
    "Колос": 37,
    "Маріуполь": 31
}

def display_teams(teams_dict):
    """Функція виведення всіх значень словника (команд і очок)"""
    if not teams_dict:
        print("Словник порожній.")
    else:
        for team, points in teams_dict.items():
            print(f"Команда: {team}, Очки: {points}")

def add_team(teams_dict):
    """Функція для додавання нової команди"""
    try:
        team_name = input("Введіть назву команди для додавання: ")
        if team_name in teams_dict:
            print(f"Команда {team_name} вже існує.")
            return
        points = input(f"Введіть кількість очок для команди {team_name}: ")
        if not points.isdigit():
            raise ValueError("Очки мають бути числом.")
        teams_dict[team_name] = int(points)
        print(f"Команду {team_name} додано з {points} очками.")
    except ValueError as e:
        print(f"Помилка: {e}")

def remove_team(teams_dict):
    """Функція для видалення команди"""
    try:
        team_name = input("Введіть назву команди для видалення: ")
        if team_name not in teams_dict:
            raise KeyError(f"Команди {team_name} не існує.")
        del teams_dict[team_name]
        print(f"Команда {team_name} була успішно видалена.")
    except KeyError as e:
        print(f"Помилка: {e}")

def view_sorted_teams(teams_dict):
    """Функція для перегляду команд за відсортованими ключами"""
    sorted_teams = sorted(teams_dict.keys())
    if not sorted_teams:
        print("Словник порожній.")
    else:
        for team in sorted_teams:
            print(f"Команда: {team}, Очки: {teams_dict[team]}")

def find_top_teams(teams_dict):
    """Функція для визначення чемпіона, а також команд на 2 та 3 місцях"""
    sorted_teams = sorted(teams_dict.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_teams) < 3:
        print("Недостатньо команд для визначення перших трьох місць.")
    else:
        print(f"Чемпіон: {sorted_teams[0][0]}, Очки: {sorted_teams[0][1]}")
        print(f"Друге місце: {sorted_teams[1][0]}, Очки: {sorted_teams[1][1]}")
        print(f"Третє місце: {sorted_teams[2][0]}, Очки: {sorted_teams[2][1]}")

def exit_program():
    """Функція для завершення програми"""
    print("Вихід з програми.")
    exit()

def main():
    """Головна функція для керування програмою"""
    menu_actions = {
        "1": display_teams,
        "2": add_team,
        "3": remove_team,
        "4": view_sorted_teams,
        "5": find_top_teams,
        "6": exit_program
    }

    while True:
        print("\n--- Меню ---")
        print("1. Вивести всі команди та їх очки")
        print("2. Додати нову команду")
        print("3. Видалити команду")
        print("4. Переглянути команди за відсортованими ключами")
        print("5. Визначити чемпіона та призерів")
        print("6. Вийти")

        choice = input("Оберіть дію (1-6): ")

        action = menu_actions.get(choice)
        if action:
            action(teams)
            input("\nНатисніть Enter, щоб повернутися до меню.")
        else:
            print("Невірний вибір, спробуйте ще раз.")

main()

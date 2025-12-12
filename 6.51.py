from rich.console import Console
from rich.table import Table
import msvcrt

console = Console()

db = [
    {
        "Прізвище": "Ді Капріо",
        "Ім'я": "Леонардо",
        "вік": 49,
        "кількість фільмів": 40,
        "статки": 300.0
    },
    {
        "Прізвище": "Хенкс",
        "Ім'я": "Том",
        "вік": 67,
        "кількість фільмів": 85,
        "статки": 400.0
    },
    {
        "Прізвище": "Йоханссон",
        "Ім'я": "Скарлетт",
        "вік": 39,
        "кількість фільмів": 60,
        "статки": 180.0
    },
    {
        "Прізвище": "Роббі",
        "Ім'я": "Марго",
        "вік": 33,
        "кількість фільмів": 35,
        "статки": 40.0
    },
    {
        "Прізвище": "Вашингтон",
        "Ім'я": "Дензел",
        "вік": 69,
        "кількість фільмів": 55,
        "статки": 280.0
    }
]

headers = list(db[0].keys())

while True:
    print("\n--- Меню Бази Даних (Актори) ---")
    print("1 - Друк списку")
    print("2 - Додати елемент до списку")
    print("3 - Відсортувати список за заданим атрибутом")
    print("4 - Видалити елемент за заданим індексом")
    print("5 - Видалити елемент за заданим атрибутом")
    print("6 - Вивести елементи із заданим атрибутом")
    print("7 - Вихід")

    print("Натисніть цифру (1-7) для вибору: ", end='', flush=True)
    key_press = msvcrt.getch()
    try:
        choice = key_press.decode('utf-8')
        print(choice)
    except UnicodeDecodeError:
        choice = ''
        print("?")

    if choice == '1':
        print("\n База даних акторів ")
        table = Table(title="Актори Голлівуду", header_style="bold green", show_lines=True)
        table.add_column("N", style="bold yellow")
        for header in headers:
            table.add_column(header.capitalize(), style="magenta")

        for i, record in enumerate(db, 1):
            row_values = [str(record.get(h, '')) for h in headers]
            table.add_row(str(i), *row_values)
        console.print(table, justify="center")

    elif choice == "2":
        print("\n Додавання нового актора ")

        new_record = {}

        try:
            for header in headers:
                val_input = input(f"Введіть '{header}': ")

                if header in ["вік", "кількість фільмів"]:
                    if not val_input.isdigit():
                        raise ValueError(f"Поле '{header}' має бути цілим числом.")

                    value = int(val_input)

                elif header == "статки":
                    try:
                        value = float(val_input)

                    except ValueError:
                        raise ValueError(f"Поле '{header}' має бути числом.")

                else:
                    value = val_input

                new_record[header] = value

            db.append(new_record)
            console.print(
                f"\n[green]Актора '{new_record['Прізвище']} {new_record["Ім'я"]}' успішно додано![/green]"
            )

        except ValueError as ve:
            console.print(f"\n[bold red]Помилка введення: {ve}[/bold red]")

        except Exception as e:
            console.print(f"\n[bold red]Сталася помилка: {e}[/bold red]")

    elif choice == '3':
        print("\n Сортування списку")
        print("За яким атрибутом сортувати:")
        for i, header in enumerate(headers):
            print(f"{i+1} - {header}")

        print("Натисніть цифру атрибуту (1-5): ", end='', flush=True)
        attr_key = msvcrt.getch()
        try:
            attr_choice = attr_key.decode('utf-8')
            print(attr_choice)
            sort_key_index = int(attr_choice) - 1
            if not (0 <= sort_key_index < len(headers)):
                raise ValueError
            sort_key = headers[sort_key_index]
        except (UnicodeDecodeError, ValueError):
            print("\n[red]Помилка: Невірний вибір атрибута.[/red]")
            continue

        try:
            N = len(db)
            for i in range(N - 1):
                for j in range(N - 1 - i):
                    if db[j][sort_key] > db[j + 1][sort_key]:
                        db[j], db[j + 1] = db[j + 1], db[j]

            print(f"\nСписок успішно відсортовано за атрибутом: '{sort_key}'")
        except Exception as e:
            print(f"\n[red]Помилка сортування: {e}[/red]")

    elif choice == '4':
        print("\n Видалення за індексом ")
        idx_to_del_str = input("Введіть номер для видалення (починаючи з 1): ")
        try:
            idx_to_del = int(idx_to_del_str)
            if 1 <= idx_to_del <= len(db):
                deleted_record = db.pop(idx_to_del - 1)
                print(f"Успішно видалено запис: {deleted_record.get('Прізвище', 'N/A')}")
            else:
                print("Помилка: Індекс виходить за межі списку.")
        except ValueError:
            print("Помилка: Введено не число.")

    elif choice == '5':
        print("\n Видалення за значенням атрибута ")
        print("За яким атрибутом видаляти:")
        for i, header in enumerate(headers):
            print(f"{i+1} - {header}")

        print("Натисніть цифру атрибуту (1-5): ", end='', flush=True)
        attr_key = msvcrt.getch()
        try:
            attr_choice = attr_key.decode('utf-8')
            print(attr_choice)
            attr_index = int(attr_choice) - 1
            if not (0 <= attr_index < len(headers)):
                raise ValueError
            delete_key = headers[attr_index]
        except (UnicodeDecodeError, ValueError):
            print("\n[red]Помилка: Невірний вибір атрибута.[/red]")
            continue

        value_to_find = input(f"Введіть значення для '{delete_key}', яке потрібно видалити: ").lower()

        new_db = []
        deleted_count = 0
        for record in db:
            if str(record.get(delete_key, '')).lower() == value_to_find:
                deleted_count += 1
            else:
                new_db.append(record)
        db = new_db
        print(f"Видалено {deleted_count} елементів.")

    elif choice == '6':
        print("\n Пошук за значенням атрибута ")
        print("За яким атрибутом шукати:")
        for i, header in enumerate(headers):
            print(f"{i+1} - {header}")

        print("Натисніть цифру атрибуту (1-5): ", end='', flush=True)
        attr_key = msvcrt.getch()
        try:
            attr_choice = attr_key.decode('utf-8')
            print(attr_choice)
            attr_index = int(attr_choice) - 1
            if not (0 <= attr_index < len(headers)):
                raise ValueError
            search_key = headers[attr_index]
        except (UnicodeDecodeError, ValueError):
            print("\n[red]Помилка: Невірний вибір атрибута.[/red]")
            continue

        value_to_find = input(f"Введіть значення для пошуку в '{search_key}': ").lower()

        print(f"\n Результати пошуку: '{search_key}' містить '{value_to_find}' ")
        table = Table(title="Результати пошуку", header_style="bold green", show_lines=True)
        table.add_column("N", style="bold yellow")
        for header in headers:
            table.add_column(header, style="magenta")

        found_count = 0
        for i, record in enumerate(db, 1):
            if value_to_find in str(record.get(search_key, '')).lower():
                row_values = [str(record.get(h, '')) for h in headers]
                table.add_row(str(i), *row_values)
                found_count += 1

        if found_count > 0:
            console.print(table, justify="center")
        else:
            print("Нічого не знайдено.")

    elif choice == '7':
        print("Завершення роботи програми...")
        break

    else:
        print("\nПомилка: Невірна команда. Будь ласка, введіть цифру від 1 до 7.")
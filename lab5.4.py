import keyboard
import time
from rich.console import Console
from rich.table import Table

console = Console()

database = [
    ["Джонсон", "Двейн", 51, 52, 800000000],
    ["Хенкс", "Том", 67, 70, 400000000],
    ["Ді Капріо", "Леонардо", 49, 40, 300000000],
    ["Йохансон", "Скарлетт", 39, 50, 165000000],
    ["Пітт", "Бред", 60, 60, 400000000],
]

columns = ["Прізвище", "Ім'я", "Вік", "К-сть фільмів", "Статки ($)"]

while True:
    console.print("\n[bold cyan]--- ГОЛОВНЕ МЕНЮ ---[/bold cyan]")
    console.print("[green]1[/green] - Друк списку")
    console.print("[green]2[/green] - Додати елемент до списку")
    console.print(
        "[green]3[/green] - Відсортувати список за заданим атрибутом (Бульбашка)"
    )
    console.print("[green]4[/green] - Видалити елемент за заданим атрибутом")
    console.print("[green]5[/green] - Видалити елемент за заданим індексом")
    console.print("[green]6[/green] - Вивести елементи із заданим атрибутом")
    console.print("[red]7[/red] - Вихід")
    console.print("\n[dim]Натисніть відповідну цифру...[/dim]")

    event = keyboard.read_event(suppress=True)
    if event.event_type == keyboard.KEY_DOWN:
        choice = event.name
        time.sleep(0.3)

        if choice == "1":
            table = Table(title="База даних: Актори")
            table.add_column("№", style="dim", width=3)
            table.add_column("Прізвище", style="magenta")
            table.add_column("Ім'я", style="cyan")
            table.add_column("Вік", justify="right")
            table.add_column("Фільми", justify="right")
            table.add_column("Статки", style="green", justify="right")

            for idx, row in enumerate(database, 1):
                formatted_money = f"${row[4]:,}"
                table.add_row(
                    str(idx),
                    str(row[0]),
                    str(row[1]),
                    str(row[2]),
                    str(row[3]),
                    formatted_money,
                )

            console.print(table)

        elif choice == "2":
            console.print("\n[bold yellow]Додавання нового актора:[/bold yellow]")
            try:
                surname = input("Введіть прізвище: ")
                name = input("Введіть ім'я: ")
                age = int(input("Введіть вік: "))
                films = int(input("Введіть кількість фільмів: "))
                wealth = int(input("Введіть статки (числом без $): "))

                database.append([surname, name, age, films, wealth])
                console.print("[bold green]Запис додано![/bold green]")
            except ValueError:
                console.print(
                    "[bold red]Помилка! Числові поля введені некоректно.[/bold red]"
                )

        elif choice == "3":
            console.print("\n[bold cyan]Оберіть атрибут для сортування:[/bold cyan]")
            for i, col in enumerate(columns, 1):
                console.print(f"[green]{i}[/green] - {col}")

            console.print("[dim]Натисніть цифру...[/dim]")

            attr_event = keyboard.read_event(suppress=True)
            if attr_event.event_type == keyboard.KEY_DOWN:
                attr_choice = attr_event.name
                time.sleep(0.3)

                if attr_choice in ["1", "2", "3", "4", "5"]:
                    col_idx = int(attr_choice) - 1

                    n = len(database)
                    for i in range(n - 1):
                        for j in range(n - i - 1):
                            should_swap = False

                            val1 = database[j][col_idx]
                            val2 = database[j + 1][col_idx]

                            if col_idx == 4:
                                if (
                                    val1 < val2
                                ):
                                    should_swap = True
                            else:
                                if (
                                    val1 > val2
                                ):
                                    should_swap = True

                            if should_swap:
                                temp = database[j]
                                database[j] = database[j + 1]
                                database[j + 1] = temp

                    console.print(
                        f"[bold green]Список успішно відсортовано (Bubble Sort) за полем: {columns[col_idx]}[/bold green]"
                    )
                else:
                    console.print("[bold red]Невірний вибір атрибуту[/bold red]")

        elif choice == "4":
            console.print("\n[bold cyan]Оберіть атрибут для видалення:[/bold cyan]")
            for i, col in enumerate(columns, 1):
                console.print(f"[green]{i}[/green] - {col}")

            attr_event = keyboard.read_event(suppress=True)
            if attr_event.event_type == keyboard.KEY_DOWN:
                attr_choice = attr_event.name
                time.sleep(0.3)

                if attr_choice in ["1", "2", "3", "4", "5"]:
                    col_idx = int(attr_choice) - 1
                    search_val = input(
                        f"Введіть значення для {columns[col_idx]}, яке треба видалити: "
                    )

                    if col_idx in [2, 3, 4]:
                        try:
                            search_val = int(search_val)
                        except ValueError:
                            console.print("[red]Потрібно ввести число![/red]")
                            continue

                    initial_len = len(database)
                    database = [row for row in database if row[col_idx] != search_val]
                    deleted_count = initial_len - len(database)

                    if deleted_count > 0:
                        console.print(
                            f"[bold green]Видалено {deleted_count} записів.[/bold green]"
                        )
                    else:
                        console.print("[yellow]Співпадінь не знайдено.[/yellow]")

        elif choice == "5":
            console.print("\n[bold yellow]Видалення за номером:[/bold yellow]")
            try:
                idx_input = int(input(f"Введіть номер рядка (1-{len(database)}): "))
                real_idx = idx_input - 1
                if 0 <= real_idx < len(database):
                    removed = database.pop(real_idx)
                    console.print(
                        f"[bold green]Видалено: {removed[0]} {removed[1]}[/bold green]"
                    )
                else:
                    console.print("[bold red]Такого номера не існує.[/bold red]")
            except ValueError:
                console.print("[bold red]Введіть коректне число.[/bold red]")

        elif choice == "6":
            console.print("\n[bold cyan]Оберіть атрибут для пошуку:[/bold cyan]")
            for i, col in enumerate(columns, 1):
                console.print(f"[green]{i}[/green] - {col}")

            attr_event = keyboard.read_event(suppress=True)
            if attr_event.event_type == keyboard.KEY_DOWN:
                attr_choice = attr_event.name
                time.sleep(0.3)

                if attr_choice in ["1", "2", "3", "4", "5"]:
                    col_idx = int(attr_choice) - 1
                    search_val = input(f"Введіть значення для {columns[col_idx]}: ")

                    if col_idx in [2, 3, 4]:
                        try:
                            search_val = int(search_val)
                        except ValueError:
                            console.print("[red]Це поле вимагає число![/red]")
                            continue

                    found_rows = [row for row in database if row[col_idx] == search_val]

                    if found_rows:
                        table = Table(
                            title=f"Результати пошуку ({columns[col_idx]} = {search_val})"
                        )
                        table.add_column("Прізвище", style="magenta")
                        table.add_column("Ім'я", style="cyan")
                        table.add_column("Вік", justify="right")
                        table.add_column("Фільми", justify="right")
                        table.add_column("Статки", style="green", justify="right")

                        for row in found_rows:
                            table.add_row(
                                str(row[0]),
                                str(row[1]),
                                str(row[2]),
                                str(row[3]),
                                f"${row[4]:,}",
                            )
                        console.print(table)
                    else:
                        console.print("[yellow]Нічого не знайдено.[/yellow]")

        elif choice == '7' or choice.lower() == 'q':
            console.print("[bold red]Роботу завершено.[/bold red]")
            break
import csv
from rich.console import Console
from rich.table import Table

console = Console()
file_name = r"C:\Users\vakhd\Downloads\log_file_29 (2).csv"

with open(file_name, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = list(next(reader))
    logs = list(list(row) for row in reader)

console.print(
    "\n[bold cyan] Пошук підозрілих користувачів [/bold cyan]"
)

logs.sort(key=lambda x: x[0])

suspicious_users = []
i = 0
n = len(logs)

while i < n:
    current_user = logs[i][0].strip()
    fail_count = 0

    j = i
    while j < n and logs[j][0].strip() == current_user:
        status = logs[j][3].strip()
        if status == "fail":
            fail_count += 1
        j += 1

    if fail_count >= 6:
        suspicious_users.append(current_user)
    i = j

console.print(f"Знайдено користувачів: {len(suspicious_users)}\n")

for user in suspicious_users:
    table = Table(
        title=f"Логи юзера: [bold yellow]{user}[/bold yellow]",
        show_header=True,
        header_style="bold magenta",
    )
    for col in header:
        table.add_column(col)
    user_logs = [row for row in logs if row[0].strip() == user]
    for log in user_logs:
        status = log[3].strip()
        style = "[red]" if status == "fail" else "[green]"
        table.add_row(
            log[0], log[1], log[2], f"{style}{status}{style.replace('[', '[/')}"
        )
    console.print(table)
console.print("\n[bold cyan] Пошук підозрілих IP-адрес [/bold cyan]")

logs.sort(key=lambda x: x[2])

suspicious_ips = []
i = 0
n = len(logs)

while i < n:
    current_ip = logs[i][2].strip()

    unique_users_on_this_ip = []
    j = i
    while j < n and logs[j][2].strip() == current_ip:
        user = logs[j][0].strip()

        is_new = True
        for u in unique_users_on_this_ip:
            if u == user:
                is_new = False
                break

        if is_new:
            unique_users_on_this_ip.append(user)

        j += 1

    if len(unique_users_on_this_ip) >= 3:
        suspicious_ips.append(current_ip)

    i = j

console.print(f"Знайдено IP-адрес: {len(suspicious_ips)}\n")

for ip in suspicious_ips:
    table = Table(
        title=f"Логи IP: [bold yellow]{ip}[/bold yellow]",
        show_header=True,
        header_style="bold magenta",
    )
    for col in header:
        table.add_column(col)

    ip_logs = [row for row in logs if row[2].strip() == ip]
    for log in ip_logs:
        status = log[3].strip()
        style = "[red]" if status == "fail" else "[green]"
        table.add_row(log[0], log[1], log[2], f"{style}{status}{style.replace('[', '[/')}")
    console.print(table)
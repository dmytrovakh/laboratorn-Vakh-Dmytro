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

logs.sort()

suspicious_users = []
i = 0
n = len(logs)

while i < n:
    current_user = logs[i][0].strip()
    fail_count = 0

    j = i
    while j < n and logs[j][0].strip() == current_user:
        if logs[j][3].strip() == "fail":
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

    for log in logs:
        if log[0].strip() == user:
            status = log[3].strip()
            style = "[red]" if status == "fail" else "[green]"
            table.add_row(
                log[0], log[1], log[2], f"{style}{status}{style.replace('[', '[/')}"
            )
    console.print(table)


console.print("\n[bold cyan] Пошук підозрілих IP-адрес [/bold cyan]")

logs_by_ip = []
for row in logs:
    logs_by_ip.append([row[2], row[0], row[1], row[3]])

logs_by_ip.sort()

suspicious_ips = []
i = 0
n = len(logs_by_ip)

while i < n:
    current_ip = logs_by_ip[i][0].strip()

    unique_users = []

    j = i
    while j < n and logs_by_ip[j][0].strip() == current_ip:
        user = logs_by_ip[j][1].strip()

        is_new = True
        for u in unique_users:
            if u == user:
                is_new = False
                break
        if is_new:
            unique_users.append(user)

        j += 1

    if len(unique_users) >= 3:
        suspicious_ips.append(current_ip)

    i = j

console.print(f"Знайдено IP-адрес: {len(suspicious_ips)}")

for ip in suspicious_ips:
    table = Table(
        title=f"Логи IP: [bold yellow]{ip}[/bold yellow]",
        show_header=True,
        header_style="bold magenta",
    )
    for col in header:
        table.add_column(col)

    for log in logs_by_ip:
        if log[0].strip() == ip:
            user_val = log[1]
            time_val = log[2]
            ip_val = log[0]
            status_val = log[3].strip()

            style = "[red]" if status_val == "fail" else "[green]"
            table.add_row(user_val, time_val, ip_val, f"{style}{status_val}{style.replace('[', '[/')}")
    console.print(table)
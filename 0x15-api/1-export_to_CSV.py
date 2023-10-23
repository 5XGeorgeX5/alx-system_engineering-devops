#!/usr/bin/python3
"""returns information about employee's TODO list using a REST API."""
from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users/"
    todo = "https://jsonplaceholder.typicode.com/todos?userId="
    name = get(user + argv[1]).json().get('name')
    tasks = get(todo + argv[1]).json()
    with open(f"{argv[1]}.csv", 'w') as file:
        csv_file = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            status = task.get('completed')
            title = task.get('title')
            csv_file.writerow([argv[1], name, status, title])

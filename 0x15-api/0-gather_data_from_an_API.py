#!/usr/bin/python3
"""returns information about employee's TODO list using a REST API."""
from requests import get
from sys import argv

if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users/"
    todo = "https://jsonplaceholder.typicode.com/todos?userId="
    name = get(user + argv[1]).json().get('name')
    tasks = get(todo + argv[1]).json()
    done = [task.get('title') for task in tasks if task.get('completed')]
    print(f"Employee {name} is done with tasks({len(done)}/{len(tasks)}):")
    for task in done:
        print(f"\t {task}")

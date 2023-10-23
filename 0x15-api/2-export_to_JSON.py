#!/usr/bin/python3
"""returns information about employee's TODO list using a REST API."""
from requests import get
from sys import argv
import json

if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users/"
    todo = "https://jsonplaceholder.typicode.com/todos?userId="
    username = get(user + argv[1]).json().get('username')
    tasks = get(todo + argv[1]).json()
    data = {argv[1]: [{
        "task": task.get('title'),
        "completed": task.get('completed'),
        "username": username
    } for task in tasks]}
    with open(f"{argv[1]}.json", 'w') as file:
        json.dump(data, file)

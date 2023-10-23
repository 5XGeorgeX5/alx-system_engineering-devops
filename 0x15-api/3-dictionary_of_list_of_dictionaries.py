#!/usr/bin/python3
"""returns information about employee's TODO list using a REST API."""
from requests import get
import json

if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users/"
    todo = "https://jsonplaceholder.typicode.com/todos?userId="
    employees = get(user).json()
    tasks = get(todo).json()
    data = {
        str(employee.get('id')): [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee.get('username')
        } for task in get(f"{todo}{employee.get('id')}").json()]
        for employee in employees
    }
    with open("todo_all_employees.json", 'w') as file:
        json.dump(data, file)

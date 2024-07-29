#!/usr/bin/python3
'''
This script uses a REST API to retrieve information
about an employee's TODO list progress
'''

import json
from requests import get
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: ./2-export_to_JSON.py <user_id>")
        exit(1)

    user_id = argv[1]

    # Retrieve TODOs and user data
    todos_res = get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    employee_res = get(f'https://jsonplaceholder.typicode.com/users/{user_id}')

    if todos_res.status_code != 200:
        print(f"Error fetching todos for user ID {user_id}")
        exit(1)
    
    if employee_res.status_code != 200:
        print(f"Error fetching user data for user ID {user_id}")
        exit(1)

    todos = todos_res.json()
    tasks_dict = {}
    tasks_list = []

    try:
        employee_username = employee_res.json()['username']
    except KeyError:
        print(f"Username not found for user ID {user_id}")
        exit(1)

    filename = f'{user_id}.json'

    for task in todos:
        new_dict = {}
        new_dict['task'] = task['title']
        new_dict['completed'] = task['completed']
        new_dict['username'] = employee_username
        tasks_list.append(new_dict)

    tasks_dict[f'{user_id}'] = tasks_list

    with open(filename, 'w') as file:
        json.dump(tasks_dict, file, indent=4)  # Use indent for pretty printing

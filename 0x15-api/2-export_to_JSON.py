#!/usr/bin/python3
'''
This script uses a REST API to retrieve information
about an employees TODO list progress
'''

import json
from requests import get
from sys import argv

if __name__ == '__main__':
    id = argv[1]
    todos_res = get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    employee_res = get(f'https://jsonplaceholder.typicode.com/users/{id}')

    todos = todos_res.json()
    tasks_dict = {}
    tasks_list = []
    employee_username = employee_res.json()['username']
    filename = f'{id}.json'

    for task in todos:
        new_dict = {}
        new_dict['task'] = task['title']
        new_dict['completed'] = task['completed']
        new_dict['username'] = employee_username
        tasks_list.append(new_dict)

    tasks_dict[f'{id}'] = tasks_list

    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)

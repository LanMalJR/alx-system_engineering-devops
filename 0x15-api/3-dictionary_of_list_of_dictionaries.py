#!/usr/bin/python3
'''
This script uses a REST API to retrieve information
about all employees TODO list progress
'''

import json
from requests import get

if __name__ == '__main__':
    tasks_dict = {}
    filename = 'todo_all_employees.json'

    for id in range(1, 11):
        t_res = get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
        employee_res = get(f'https://jsonplaceholder.typicode.com/users/{id}')

        todos = t_res.json()
        tasks_list = []
        employee_username = employee_res.json()['username']

        for task in todos:
            new_dict = {}
            new_dict['task'] = task['title']
            new_dict['completed'] = task['completed']
            new_dict['username'] = employee_username
            tasks_list.append(new_dict)

        tasks_dict[f'{id}'] = tasks_list

    with open(filename, 'w') as file:
        json.dump(tasks_dict, file)

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
    total_tasks = len(todos)
    completed_tasks_len = 0
    completed_tasks_list = []
    employee_name = employee_res.json()['name']

    for task in todos:
        if task['completed'] is True:
            completed_tasks_len += 1
            completed_tasks_list.append(task['title'])

    print('Employee {} is done with tasks({}/{}):'.
          format(employee_name,
                 completed_tasks_len,
                 total_tasks))

    for task in completed_tasks_list:
        print(f'\t {task}')

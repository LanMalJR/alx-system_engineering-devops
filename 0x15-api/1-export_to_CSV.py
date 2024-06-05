#!/usr/bin/python3
'''
This script uses a REST API to retrieve information
about an employees TODO list progress and save it to a CSV file
'''

from requests import get
from sys import argv

if __name__ == '__main__':
    id = argv[1]
    todos_res = get(f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    employee_res = get(f'https://jsonplaceholder.typicode.com/users/{id}')

    todos = todos_res.json()
    employee_username = employee_res.json()['username']
    filename = f'{id}.csv'

    with open(filename, 'w') as file:
        for task in todos:
            row = '"{}","{}","{}","{}"\n'.format(
                    id,
                    employee_username,
                    task['completed'],
                    task['title']
                    )
            file.write(row)

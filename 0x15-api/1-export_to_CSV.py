#!/usr/bin/python3
"""
    Task 1
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    # Checking
    if len(argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        exit(1)

    employee_id = argv[1]

    rusr = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    rtodo = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(employee_id))

    jusr = rusr.json()
    jtodo = rtodo.json()

    name = jusr.get('username')
    fname = '{}.csv'.format(employee_id)

    with open(fname, mode='w') as user_file:
        user_writer = csv.writer(user_file, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_ALL)
        for t in jtodo:
            user_writer.writerow([employee_id, name, t.get('completed'),
                                  t.get('title')])

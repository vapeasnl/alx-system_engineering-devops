#!/usr/bin/python3
# Write a Python script that, using this REST API

import requests
import sys


if __name__ == "__main__":
    # Check if the script is provided with an employee ID
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_ID = sys.argv[1]
    jsonplaceholder = 'https://jsonplaceholder.typicode.com/users'
    url = f'{jsonplaceholder}/{employee_ID}'

    # Make a GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        employee_name = response.json().get('name')
        Todourl = f'{url}/todos'
        res = requests.get(Todourl)
        tasks = res.json()

        # completed tasks
        done_tasks = [task for task in tasks if task.get('completed')]

        # Display the employee TODO list
        print("Employee {} is done with tasks({}/{}):".format(employee_name, len(done_tasks), len(tasks)))
        for task in done_tasks:
            print("\t{}".format(task.get('title')))
    else:
        # Display an error message if the request not successful
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")


#!/usr/bin/python3
"""
    Task api 1
"""

import csv
import requests
import sys import argv


def export_employee_todo_csv(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Retrieve employee information
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()

        # Retrieve employee's TODO list
        response = requests.get(todos_url)
        response.raise_for_status()
        todos_data = response.json()

        # Extract relevant information
        user_id = employee_data['id']
        username = employee_data['username']

        # Prepare CSV file name
        file_name = f"{user_id}.csv"

        # Prepare data for CSV export
        csv_data = []
        for todo in todos_data:
            task_completed_status = "True" \
                if todo['completed'] else "False"
            task_title = todo['title']
            csv_data.append([
                user_id, username, task_completed_status, task_title])

        # Export data to CSV file
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerows(csv_data)

        print(f"CSV file '{file_name}' exported successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")
        return


if __name__ == '__main__':
    employee_id = sys.argv[1]
    export_employee_todo_csv(employee_id)

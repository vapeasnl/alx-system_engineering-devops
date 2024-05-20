#!/usr/bin/python3
# Using what i did in the task #0

import json
import requests


if __name__ == '__main__':
    rusr = requests.get('https://jsonplaceholder.typicode.com/users')
    jusr = rusr.json()
    retd = dict()
    for usr in jusr:
        ul = []
        uid = usr.get('id')
        uname = usr.get('username')
        rtodo = requests.get('https://jsonplaceholder.typi' +
                             'code.com/users/{}/todos'.format(uid))
        for do in rtodo.json():
            ul.append({"username": uname, "task": do.get('title'), "completed":
                      do.get('completed')})
        retd.update({uid: ul})

    fname = "todo_all_employees.json"
    with open(fname, mode='w') as user_file:
        json.dump(retd, user_file, sort_keys=True)

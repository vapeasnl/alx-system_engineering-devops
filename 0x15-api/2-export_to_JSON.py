#!/usr/bin/python3
# Using what i did in the task #0

import json
import requests
from sys import argv

if __name__ == '__main__':
    rusr = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    rtodo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(argv[1]))
    jusr = rusr.json()
    jtodo = rtodo.json()

    done = len(jtodo)
    notdone = 0
    uname = jusr.get('username')
    name = jusr.get('name')
    fname = argv[1] + ".json"

    retd = dict()
    retl = []
    for t in jtodo:
        retl.append({"task": t.get('title'), "completed": t.get('completed'),
                    "username": uname})
    retd.update({argv[1]: retl})
    with open(fname, mode='w') as user_file:
        json.dump(retd, user_file)

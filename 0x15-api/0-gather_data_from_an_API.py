#!/usr/bin/python3
"""
    Task api 0
"""
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
    name = jusr.get('name')
    for t in jtodo:
        if t.get('completed') is True:
            notdone = notdone + 1

    print("Employee {} is done with tasks({}/{}):".format(name, notdone, done))
    for t in jtodo:
        if t.get('completed') is True:
            print("\t {}".format(t.get('title')))

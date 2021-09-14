#!/usr/bin/python3
"""
This script return information about his/her todo list
"""


import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]

    rsp = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(id))
    rsp2 = requests.get(
        "https://jsonplaceholder.typicode.com/todos")

    name = rsp.json()["name"]

    done_task = 0
    total_task = 0
    title_list = []

    for task in rsp2.json():
        if task.get("userId") == int(id):
            if task.get('completed'):
                done_task += 1
                title_list.append("\t " + task.get("title"))
            total_task += 1

    print("Employee {} is done with task({}/{}):".format(name,
                                                         done_task,
                                                         total_task))
    print('\n'.join(title_list))

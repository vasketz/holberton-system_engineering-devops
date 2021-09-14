#!/usr/bin/python3
"""
This script return information about his/her todo list
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    users = "https://jsonplaceholder.typicode.com/users/"\
            + argv[1]
    todos = "https://jsonplaceholder.typicode.com/users/"\
            + argv[1] + "/todos"

    fd = argv[1] + ".json"
    rsp = requests.get(users)
    rsp2 = requests.get(todos)
    array = []
    for value in rsp2.json():
        array.append({"task": value.get("title"),
                      "completed": value.get("completed"),
                      "username": rsp.json().get("username")})
    j_file = {argv[1]: array}
    with open(fd, mode="w") as json_file:
        json_file.write(json.dumps(j_file))

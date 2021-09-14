#!/usr/bin/python3
"""
This script return information about his/her todo list
"""


import csv
from os import write
import requests
from sys import argv


if __name__ == "__main__":
    users = "https://jsonplaceholder.typicode.com/users/"\
            + argv[1]
    todos = "https://jsonplaceholder.typicode.com/users/"\
            + argv[1] + "/todos"

    fd = argv[1] + ".csv"
    rsp = requests.get(users)
    rsp2 = requests.get(todos)
    username = rsp.json().get("username")
    with open(fd, mode="w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for value in rsp2.json():
            writer.writerow([str(value.get("userId")),
                            username,
                            str(value.get("completed")),
                            value.get("title")])

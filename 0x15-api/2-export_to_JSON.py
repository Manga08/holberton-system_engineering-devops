#!/usr/bin/python3
"""Using a REST API, for a given employee ID,export data in the JSON format."""
import requests
from sys import argv
import json
import requests
import sys


if __name__ == "__main__":
    employee = sys.argv[1]
    URL = 'https://jsonplaceholder.typicode.com/'
    URL_User = URL + 'users/' + employee
    resp = requests.get(URL_User)
    Name = resp.json().get('username')
    URL_User = URL + 'todos'
    resp = requests.get(URL_User)
    info = [task for task in resp.json()
            if task.get('userId') is int(employee)]
    listy = []

    for data in info:
        new_dict = {"task": data['title'],
                    "completed": data['completed'],
                    "username": Name}
        listy.append(new_dict)
    dicty = {sys.argv[1]: listy}
    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        json.dump(dicty, f)

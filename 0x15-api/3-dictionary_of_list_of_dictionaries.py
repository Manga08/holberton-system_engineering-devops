#!/usr/bin/python3
"""Using a REST API, for a given employee ID"""
import json
import requests


if __name__ == "__main__":
    URL = 'https://jsonplaceholder.typicode.com/'
    URL_User = URL + 'users/'
    resp_User = requests.get(URL_User)
    users = resp_User.json()
    users_dicty = {}
    for current_user in users:
        URL = URL + 'todos'
        resp = requests.get(URL)
        employee = current_user.get('id')
        data = [info for info in resp.json()
                 if info.get('userId') is int(employee)]
        list = []
        for info in data:
            new_dicty = {"username": current_user['username'],
                        "task": info['title'],
                        "completed": info['completed'],
                        }
            list.append(new_dicty)
        users_dicty[current_user.get('id')] = list

    with open('{}.json'.format('todo_all_employees'), 'w') as f:
        json.dump(users_dicty, f)

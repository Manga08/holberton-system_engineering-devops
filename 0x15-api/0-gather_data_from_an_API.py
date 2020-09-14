#!/usr/bin/python3
"""Using this REST API, for a given employee ID."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        URL_user = "https://jsonplaceholder.typicode.com/users/" + argv[1]
        resp = requests.get(URL_user)
        dicty = json.loads(resp.text)
        get_name = dicty.get('name')
        URL_User_ID = "https://jsonplaceholder.typicode.com/todos/?userId="\
            + argv[1]
        resp_ID = requests.get(URL_User_ID)
        info = json.loads(resp_ID.text)
        Full_Dicty = []
        for data in info:
            if data.get('completed'):
                Full_Dicty.append(data)
        print("info {} is done with datas({}/{}):".
              format(get_name, len(Full_Dicty), len(info)))
        for data in Full_Dicty:
            print('\t {}'.format(data.get('title')))

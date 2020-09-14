#!/usr/bin/python3
"""Using a REST API, for a given employee ID, export data in the CSV format."""
import csv
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

    info = [data for data in resp.json()
            if data.get('userId') is int(employee)]

    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        fields = ["name", "userId", "title", "completed"]
        writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
        for element in info:
            element['name'] = Name
            del element['id']
            writer.writerow(element)

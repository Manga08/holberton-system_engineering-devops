#!/usr/bin/python3
"""Using a REST API, for a given employee ID, export data in the CSV format."""

if __name__ == '__main__':
    import requests
    import csv
    from sys import argv

    resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1]))
    user = resp.json().get('username')

    resp = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(argv[1]))
    data = resp.json()

    with open('{}.csv'.format(argv[1]), mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in data:
            writer.writerow([argv[1], user, task.get('completed'),
                             task.get('title')])

#!/usr/bin/python3
"""Using a REST API, for a given employee ID,export data in the JSON format."""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1]))
    user = resp.json().get('username')

    resp = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(argv[1]))
    data = resp.json()

    export = {}
    export['{}'.format(argv[1])] = []
    for task in data:
        export['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user
        })
    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(export, f)

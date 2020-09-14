#!/usr/bin/python3
"""Using a REST API, for a given employee ID"""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    all_id = set()
    resp = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = resp.json()
    for user in data:
        all_id.add(user.get('userId'))

    export = {}
    for user in all_id:
        resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(user))
        user = resp.json().get('username')

        resp = requests.get('https://jsonplaceholder.typicode.com/' +
                            'todos?userId={}'.format(user))
        data = resp.json()

        export['{}'.format(user)] = []
        for task in data:
            export['{}'.format(user)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump({int(x): export[x] for x in export.keys()},
                  f, sort_keys=True)

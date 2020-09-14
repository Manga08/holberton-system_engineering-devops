#!/usr/bin/python3
"""Using this REST API, for a given employee ID."""

if __name__ == '__main__':
    import requests
    from sys import argv

    resp = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(argv[1]))
    name = resp.json().get('name')

    resp = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(argv[1]))
    data = resp.json()
    done = total = 0
    for task in data:
        total += 1
        if task.get('completed'):
            done += 1

    print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    for task in data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))

#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for in subreddit."""
    try:
        resp = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'.
                            format(subreddit),
                            headers={'User-Agent': 'custom'},
                            allow_redirects=False)
        for thread in resp.json().get('data').get('children'):
            print(thread.get('data').get('title'))
    except BaseException:
        print('None')

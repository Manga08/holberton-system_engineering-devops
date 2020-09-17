#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list."""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all hot articles."""
    try:
        resp = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                            format(subreddit, after),
                            headers={'User-Agent': 'custom'},
                            allow_redirects=False)
        if after is None:
            return hot_list
        for thread in resp.json().get('data').get('children'):
            hot_list += [thread.get('data').get('title')]
        after = resp.json().get('data').get('after')
        recurse(subreddit, hot_list, after)
        return hot_list
    except BaseException:
        return None

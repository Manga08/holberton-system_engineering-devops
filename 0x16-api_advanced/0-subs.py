#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """If an invalid subreddit is given, the function should return 0."""
    try:
        resp = requests.get('https://www.reddit.com/r/{}/about.json'.
                            format(subreddit),
                            headers={'User-Agent': 'custom'},
                            allow_redirects=False)
        return resp.json().get('data').get('subscribers')
    except BaseException:
        return 0

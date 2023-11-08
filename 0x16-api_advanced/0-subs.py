#!/usr/bin/python3
"""Script that queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-agent': 'ALX project'}

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data['data']["subscribers"]
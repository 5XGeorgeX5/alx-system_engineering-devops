#!/usr/bin/python3
"""Script that queries the Reddit API and returns a list of all hot titles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API and returns a list of all hot titles"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    url += f"&after={after}"
    header = {'User-agent': 'ALX project'}

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list

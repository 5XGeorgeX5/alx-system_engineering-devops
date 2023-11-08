#!/usr/bin/python3
"""Script that queries the Reddit API and prints the titles of the first 10"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and returns the titles of the first 10 hot"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    header = {'User-agent': 'ALX project'}

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        print('None')
        return

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        print(post['data']['title'])

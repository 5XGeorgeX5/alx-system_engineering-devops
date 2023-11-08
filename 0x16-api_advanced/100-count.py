#!/usr/bin/python3
"""Script that queries the Reddit API and returns a list of all hot titles"""
import requests


def count_words(subreddit, word_list, count={}, after=None):
    """queries the Reddit API and returns a list of all hot titles"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    url += f"&after={after}"
    header = {'User-agent': 'ALX project'}

    if not after:
        word_list = [word.lower() for word in word_list]

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        words = post['data']['title'].lower().split()
        for word in words:
            if word in word_list:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1

    after = data['data']['after']
    if after:
        return count_words(subreddit, word_list, count, after)
    sort_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sort_count:
        print(f"{key}: {value}")
    return count

#!/usr/bin/python3
"""
Write a function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    rsp = requests.get(url, headers={'user-agent': 'vasketz'},
                       allow_redirects=False)
    if rsp.status_code == 200:
        data = rsp.json().get("data").get("subscribers")
        return data
    else:
        return 0

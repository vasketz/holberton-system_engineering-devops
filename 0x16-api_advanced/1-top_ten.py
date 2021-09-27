#!/usr/bin/python3
"""
Write a function that queries the Reddit API
"""

import requests


def top_ten(subreddit):
    """ returns the number of subscribers """
    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
    rsp = requests.get(url,
                       headers={'user-agent': 'vasketz'},
                       allow_redirects=False,
                       params={"limit": 10})
    if rsp.status_code == 200:
        for element in rsp.json().get("data").get("children"):
            print(element.get("data").get("title"))
    else:
        print("None")

#!/usr/bin/python3
"""
Write a function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after="None"):
    """ returns the number of subscribers """
    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
    rsp = requests.get(url,
                       headers={'user-agent': 'vasketz'},
                       allow_redirects=False,
                       params={"after": after})
    if after is None:
        return hot_list
    elif rsp.status_code == 200:
        for element in rsp.json().get("data").get("children"):
            hot_list.append(element.get("data").get("title"))
        after = rsp.json().get("data").get("after")
        recurse(subreddit, hot_list, after=after)
    return hot_list

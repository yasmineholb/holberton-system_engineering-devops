#!/usr/bin/python3
"""reddit api """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles"""
    ur = requests.get("https://www.reddit.com/r/{}/hot.json"
                      .format(subreddit),
                      params={"after": after},
                      headers={"User-Agent": "User-Agent"})
    if ur.status_code != 200:
        return None
    ad = ur.json().get("data")
    after = ad.get("after")
    for ch in ad.get("children"):
        hot_list.append(ch.get("data").get("title"))
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list

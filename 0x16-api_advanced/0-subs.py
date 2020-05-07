#!/usr/bin/python3
"""reddit api"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    ur = requests.get("https://www.reddit.com/r/{}/about.json"
                      .format(subreddit),
                      headers={"User-Agent": "User-Agent"},
                      allow_redirects=False)
    if ur.status_code == 200:
        return ur.json().get("data").get("subscribers")
    return 0

#!/usr/bin/python3
"""reddit api"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    ur = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                      .format(subreddit),
                      headers={"User-Agent": "User-Agent"})
    if ur.status_code == 200:
        [print(t.get("data").get("title"))
         for t in ur.json().get("data").get("children")]
    else:
        print('None')

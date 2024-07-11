#!/usr/bin/python3
"""Querying the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit"""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom_user_agent/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        else:
            return 0
    except Exception:
        return 0


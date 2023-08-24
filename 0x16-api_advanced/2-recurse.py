#!/usr/bin/python3
"""Recursive function that queries the Reddit API."""
from requests import get
previous = None


def recurse(subreddit, hot_list=[]):
    """Args:
        subreddit: subreddit name
        hot_list: list of hot titles in subreddit
        after: last hot_item appended to hot_list
    Returns:
        a list containing the titles of all hot articles for the subreddit
        or None if queried subreddit is invalid."""
    global previous
    headers = {'User-Agent': 'xica369'}
    endpoint = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': previous}
    res = get(endpoint, headers=headers, allow_redirects=False,
                            params=params)

    if res.status_code == 200:
        after = res.json().get('data').get('after')
        if after is not None:
            previous = after
            recurse(subreddit, hot_list)
        list_titles = res.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)

#!/usr/bin/python3

from requests import get

def number_of_subscribers(subreddit):
    """
    - queries the Reddit API and returns the 
      number of total subscribers
    - returns 0 if not invalid subreddit
    """

    endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = get(endpoint, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json()['data']['subscribers']

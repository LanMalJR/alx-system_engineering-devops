#!/usr/bin/python3
'''
This function queries the Reddit API and returns
a list containing the titles of all hot articles
'''

import requests


def recurse(subreddit, hot_list=[], after_token=None):
    '''Returns a list of all hot articles'''

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Alx-User'}

    if after_token:
        params = {'limit': 100, 'after': after_token}
    else:
        params = {'limit': 100}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        objects = data['data']['children']

        if not objects:
            return hot_list

        for obj in objects:
            hot_list.append(obj['data']['title'])

        after_token = data['data']['after']
        if after_token is None:
            return hot_list

        return recurse(subreddit, hot_list, after_token)
    else:
        return None

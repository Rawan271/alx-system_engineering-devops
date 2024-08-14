#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my-app/0.0.1'}
    
    # Make a request to the Reddit API for the given subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and return the number of subscribers
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        # If the subreddit is invalid or not found, return 0
        return 0

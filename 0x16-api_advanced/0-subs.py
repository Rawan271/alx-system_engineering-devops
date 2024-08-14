#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'my-app/0.0.1'}

    # Construct the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        # Make the request to Reddit's API, avoid following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code is 200
        if response.status_code == 200:
            # Parse the JSON response and get the number of subscribers
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        else:
            # If the status code is not 200, return 0
            return 0
    except requests.RequestException:
        # Handle any request exceptions (e.g., connection errors)
        return 0

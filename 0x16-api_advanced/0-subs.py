#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
  """Queries the Reddit API for a subreddit's subscriber count and returns it.

  Args:
      subreddit: The name of the subreddit to query (string).

  Returns:
      The number of subscribers for the subreddit (int), or 0 if the subreddit
      is invalid or an error occurs.
  """

  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {"User-Agent": "MyCustomUserAgent (e.g., your_app_name/version)"}  # Set custom User-Agent

  try:
    response = requests.get(url, headers=headers, allow_redirects=False)  # Prevent redirects

    response.raise_for_status()  # Raise an exception for non-200 status codes

    data = response.json()
    if data.get("data", {}).get("subscribers") is not None:
      return data["data"]["subscribers"]

  except requests.exceptions.RequestException as e:
    print(f"Error querying Reddit API: {e}")

  return 0

# Example usage (assuming 0-main.py is in the same directory)
if __name__ == "__main__":
  import sys

  if len(sys.argv) < 2:
    print("Please pass an argument for the subreddit to search.")
  else:
    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)
    print(f"Subscribers   
 for '{subreddit}': {subscribers}")

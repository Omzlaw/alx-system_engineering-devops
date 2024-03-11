#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API and returns the number of subscribers for a given subreddit.

  Args:
      subreddit: The name of the subreddit (e.g., "programming").

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """

  # Set a custom User-Agent to avoid throttling
  headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
  }

  # Construct the API URL
  url = f"https://reddit.com/r/{subreddit}/about.json"

  # Send a GET request without following redirects
  response = requests.get(url, headers=headers, allow_redirects=False)

  # Check for successful response
  if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Return the number of subscribers
    return data.get("data", {}).get("subscribers", 0)
  else:
    # Invalid subreddit or error, return 0 subscribers
    return 0

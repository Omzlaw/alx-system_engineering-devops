#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
  """
  This function queries the Reddit API and prints the titles of the first 10 hot posts 
  listed for a given subreddit.

  Args:
      subreddit: The name of the subreddit (e.g., "programming").
  """

  # Set a custom User-Agent to avoid throttling
  headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
  }

  # Construct the API URL
  url = f"https://reddit.com/r/{subreddit}/hot.json"

  # Send a GET request without following redirects
  response = requests.get(url, headers=headers, allow_redirects=False)

  # Check for successful response
  if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Extract data and titles
    data = data.get("data", {})
    children = data.get("children", [])
    titles = [child.get("data", {}).get("title", "") for child in children[:10]]

    # Print the titles
    if titles:
      print(f"Top 10 Hot Posts in r/{subreddit}:")
      for title in titles:
        print(title)
    else:
      print(f"No hot articles found for subreddit: {subreddit}")
  else:
    # Invalid subreddit or error, print None
    print(None)


#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after=None):
  """
  This function recursively queries the Reddit API and returns a list containing 
  titles of all hot articles for a given subreddit.

  Args:
      subreddit: The name of the subreddit (e.g., "programming").
      hot_list (list, optional): An empty list to accumulate titles (default: []).
      after (str, optional): A marker for pagination after the previous page (default: None).

  Returns:
      A list containing titles of all hot articles or None if the subreddit is invalid.
  """

  # Set a custom User-Agent to avoid throttling
  headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
  }

  # Construct the API URL with pagination parameter (after)
  url = f"https://reddit.com/r/{subreddit}/hot.json"
  params = {'after': after} if after else {}

  # Send a GET request without following redirects
  response = requests.get(url, headers=headers, allow_redirects=False, params=params)

  # Check for successful response
  if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Extract data and titles
    data = data.get("data", {})
    after = data.get("after")
    children = data.get("children", [])
    titles = [child.get("data", {}).get("title", "") for child in children]

    # Append titles to the list and call recursively if there's more data
    hot_list.extend(titles)
    if after:
      return recurse(subreddit, hot_list, after)
    else:
      return hot_list
  else:
    # Invalid subreddit or error, return None
    return None


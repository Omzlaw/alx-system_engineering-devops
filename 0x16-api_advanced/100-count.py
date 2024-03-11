#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests
from collections import Counter

def count_words(subreddit, word_list, word_counts={}, after=None):
  """
  This function recursively queries the Reddit API, parses hot article titles, 
  and prints a sorted count of given keywords (case-insensitive).

  Args:
      subreddit: The name of the subreddit (e.g., "programming").
      word_list: A list of keywords to search for (case-insensitive).
      word_counts: A dictionary to accumulate keyword counts (default: {}).
      after (str, optional): A marker for pagination after the previous page (default: None).
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

    # Process titles and update word counts
    for child in children:
      title = child.get("data", {}).get("title", "").lower()
      for word in word_list:
        # Clean word (remove special characters)
        clean_word = ''.join(c for c in word.lower() if c.isalnum())
        if clean_word == word.lower() and title.find(clean_word) != -1:
          word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

    # Call recursively if there's more data
    if after:
      count_words(subreddit, word_list, word_counts, after)

  # Base case: After all pages or no results, process and print counts
  if not after or not response.ok:
    if word_counts:
      # Sort word counts by value (descending) and then by key (ascending)
      sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
      print(f"Word counts for r/{subreddit}:")
      for word, count in sorted_counts:
        print(f"{word}: {count}")
    else:
      print(f"No posts matching keywords found in r/{subreddit}")



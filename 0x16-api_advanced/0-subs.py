#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Splitting the User-Agent string across multiple lines
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/110.0.0.0 Safari/537.36"
    )

    headers = {"User-Agent": user_agent}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit exists (status code 404 indicates not found)
    if response.status_code == 404:
        return 0

    # Extract the number of subscribers from the response
    results = response.json().get("data")
    return results.get("subscribers")

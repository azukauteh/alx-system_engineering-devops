
```markdown
# 0x16. API advanced

Welcome to the 0x16. API advanced directory! This document will walk you through key concepts and techniques for interacting with APIs, manipulating data, and effectively utilizing advanced features. Whether you're a developer or a data enthusiast, this guide will help you become proficient in API consumption and data manipulation.

## Table of Contents

1. [Finding API Endpoints](#finding-api-endpoints)
2. [Working with Pagination](#working-with-pagination)
3. [Parsing JSON Data](#parsing-json-data)
4. [Making Recursive API Calls](#making-recursive-api-calls)
5. [Sorting a Dictionary by Value](#sorting-a-dictionary-by-value)
6. [Reddit API Documentation](#reddit-api-documentation)
7. [Query String](#query-string)
8. [Task](#Task)
9. [Requirements](#Requirements)

## 1. Finding API Endpoints

APIs typically provide a range of endpoints, each serving a specific purpose. To find the endpoints you're looking for, refer to the API documentation. The documentation will describe the available endpoints, their functionalities, and the request parameters they accept. Understanding these endpoints is fundamental to working with any API effectively.

```python
import requests

# API base URL
api_url = "https://api.example.com"

# Make a GET request to the root of the API to get endpoint information
response = requests.get(api_url)
endpoints = response.json()  # Assuming the API provides endpoint information in JSON

# Print the list of available endpoints
print(endpoints)
```

## 2. Working with Pagination

Many APIs use pagination to handle large datasets. Pagination divides data into manageable chunks, allowing you to request and process one page at a time. To work with pagination, follow the guidelines provided in the API documentation. You'll typically use query parameters like `page` or `offset` to navigate through pages and retrieve all the data.

```python
import requests

api_url = "https://api.example.com/data"
page = 1
data = []

while True:
    response = requests.get(api_url, params={"page": page})
    page_data = response.json()
    data.extend(page_data)

    if not page_data:  # No more data to retrieve
        break

    page += 1

# You now have all data in the 'data' list
```

## 3. Parsing JSON Data

JSON (JavaScript Object Notation) is a common data format used by APIs. To parse JSON results from an API, you can use various programming languages' built-in libraries or third-party packages. Typically, you'll make an API request and parse the JSON response to extract the data you need. Refer to your programming language's documentation or third-party libraries to learn how to parse JSON effectively.

```python
import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)

# Access data
print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])
```

## 4. Making Recursive API Calls

Recursive API calls are useful when dealing with hierarchical data or situations where you need to iterate through a dataset with unknown depth. To make recursive API calls, you'll create a function that calls the API and processes the data, potentially making additional calls for nested data structures. Be mindful of rate limits and request throttling when implementing recursive calls.

```python
import requests

def get_nested_data(api_url):
    response = requests.get(api_url)
    data = response.json()

    # Process data here

    if "next_page" in data:
        # Make a recursive call for the next page
        get_nested_data(data["next_page"])

# Start the recursive call with the API root URL
root_url = "https://api.example.com/nested_data"
get_nested_data(root_url)
```

## 5. Sorting a Dictionary by Value

Sorting a dictionary by its values is a common operation when working with data. Depending on your programming language, you can use built-in functions or libraries to sort a dictionary by its values in ascending or descending order. Make sure to check the documentation for your specific programming language for guidance on dictionary sorting.

```python
data = {"apple": 3, "banana": 1, "cherry": 2}

sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

# sorted_data will now contain the dictionary sorted by values
print(sorted_data)
```

## 6. Reddit API Documentation

When working with specific APIs like Reddit, refer to the Reddit API documentation for detailed information on available endpoints, authentication methods, and usage guidelines. The Reddit API documentation will provide you with the specific details required to interact with the Reddit API effectively.

```python
import requests

# Reddit API endpoint for searching subreddits
api_url = "https://www.reddit.com/subreddits/search.json"

# Construct a query string to search for subreddits related to a specific topic (e.g., "python")
query_string = "q=python"

# Make the API request
response = requests.get(f"{api_url}?{query_string}")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract and print subreddit titles
    for subreddit in data['data']['children']:
        print(subreddit['data']['display_name'])
else:
    print("API request failed with status code:", response.status_code)
```

## 7. Query String

A query string is often used in API requests to pass parameters that filter, sort, or specify the data you want to retrieve. The structure of the query string can vary between APIs, so refer to the API documentation for the correct syntax and parameters to use when constructing query strings for your requests.

```python
import requests

# URL of the API endpoint
api_url = "https://api.example.com/resource"

# Query string parameters
query_params = {
    "param1": "value1",
    "param2": "value2",
    "param3": "value3"
}

# Make the API request with the query string
response = requests.get(api_url, params=query_params)

# Check if the request was successful
if response.status_code == 200:
    # Process the API response here
    data = response.json()
    print(data)
else:
    print("API request failed with status code:", response.status_code)
```

These are basic examples to illustrate the concepts. In real-world scenarios, you'll often need to handle more complex cases and ensure error handling, authentication, and other considerations are addressed.

![Author](https://img.shields.io/badge/Author-Azuka%20Uteh-blue.svg)
```

## Tasks
The following tasks are examples of how you can interact with the Reddit API using Python. These tasks are commonly performed when working with Reddit data. Each task is associated with a Python script that accomplishes the task:

- Task 0: Count Subscribers
0-subs.py: This function queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function returns 0.

= Task 1: List Top Posts
1-top_ten.py: This function queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

= Task 2: Recursively List Hot Posts
2-recurse.py: This is a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function returns None.

- Task 3: Count Keywords in Hot Articles
100-count.py: This is a recursive function that queries the Reddit API, parses the titles of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces). For example, if you want to count the occurrences of "python" and "java" in hot articles, this script will provide the counts.

Each of these tasks demonstrates practical use cases for interacting with the Reddit API. The scripts are written in Python and utilize the requests library for making API requests.

Please ensure you have the required Python libraries installed and the necessary API credentials (if required) before running these scripts.

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Libraries imported in your Python files must be organized in alphabetical order
- Your code should use the PEP 8 style
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- You must use the Requests module for sending HTTP requests to the Reddit API
- your files will be compiled using python3 1-main.py programming

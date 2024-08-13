import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The subreddit to query.
    
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data.get('data', {}).get('subscribers', 0)
        else:
            # Return 0 for invalid subreddits or errors
            return 0
    except requests.RequestException:
        # Handle any request exceptions
        return 0

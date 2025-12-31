import requests
from datetime import datetime, timedelta

URL = "https://jsonplaceholder.typicode.com/posts"

# cache storage
posts_cache = None
cache_time = None
CACHE_DURATION_MINUTES = 5  # Cache expires after 5 minutes

# Get all posts using caching
def fetch_post():

    global posts_cache, cache_time

    # Check if cache exists and is still valid
    if posts_cache is not None and cache_time is not None:
        time_elapsed = datetime.now() - cache_time
        if time_elapsed < timedelta(minutes=CACHE_DURATION_MINUTES):
            print("Using cached data")
            return posts_cache
        else:
            print("Cache expired, fetching new data")
    
    # Fetch from API if no cache or cache expired
    print("Fetching from API...")

    response = requests.get(URL)
    if response.status_code == 200:
        posts_cache = response.json()  # Store in cache
        cache_time = datetime.now()    # Store timestamp
        print("Data cached successfully")
        return posts_cache
    else:
        print("Failed to fetch posts")
        return None
    
# Get total number of posts
def get_all_post(posts):
    if posts is None:
        return 0
    return len(posts)

# Get posts by specific user
def get_posts_by_user(posts, user_id):
    if posts is None:
        return []
    
    user_posts = []  # empty list to store user's posts

    for post in posts:
        if post["userId"] == user_id:   # Check if post belongs to the user
            user_posts.append(post)
    
    return user_posts

# Get post with longest title
def get_longest_title(posts):
    if not posts:
        return "No posts available"
     # Initialize with first post's title
    longest_title = posts[0]["title"]

    # all posts to find longest title
    for post in posts:
        # current title is longer, update longest
        if len(post["title"]) > len(longest_title):
            longest_title = post["title"]
    return longest_title

# Create a new post
def create_post():
    payload = {
        "title": "First Post",
        "body": "sample post",
        "userId": 1
    }
    response = requests.post(URL, json=payload)
    return response.json()


# Function to clear cache manually
def clear_cache():
    global posts_cache, cache_time
    posts_cache = None
    cache_time = None
    print("Cache cleared")
    
def main():
    posts = fetch_post()

    print("Fetched Posts:", fetch_post())
    print("Total Posts:", get_all_post(posts))
    print("Posts by User 1:", len(get_posts_by_user(posts, 1)))
    print("Longest Title:", get_longest_title(posts))

    new_post = create_post()
    print("\nNew Post Created:", new_post)

if __name__ == "__main__":
    main()
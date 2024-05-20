import tweepy

# Set your Twitter API credentials
consumer_key = '4dkh3VMfM2pAfsNCeSqIvH3wd'
consumer_secret = 'JOpEK2QpMOW0nSw8eil0Zbx38EFYND3AJg79gZ5sh5RI178wAO'
access_token = '1787346353649004544-WXWbGuKpGw97ORvfBqOfwi7fgLYncW'
access_token_secret = 'UQjgjitpE3ogTqT3waps2GjIxQed6fzTqMLdU8qZs4uv8'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# List of Twitter usernames to search for
usernames = ['elonmusk', 'naman_makkar_']

try:
    # Loop through each username and fetch user information
    for username in usernames:
        user = api.get_user(screen_name=username)
        followers_count = user.followers_count
        user_name = user.name
        profile_url = f"https://twitter.com/{username}"

        # Print user information
        print(f"Username: {username}")
        print(f"Followers Count: {followers_count}")
        print(f"Name: {user_name}")
        print(f"Profile URL: {profile_url}")
        print('-' * 50)

except tweepy.TweepError as e:
    print(f"An error occurred: {e}")
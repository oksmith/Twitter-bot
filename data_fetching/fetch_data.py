"""
Loading data.
"""

import tweepy

# Import the keys from a module not added to Git. Cannot let these keys be publicly accessible.
from data_fetching.keys import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Create and authenticate an API object
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Print the most recent few tweets from my timeline
public_tweets = api.home_timeline(50)
for tweet in public_tweets:
    print(tweet.user.screen_name)

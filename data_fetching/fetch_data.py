"""
Fetching image data corresponding to the last 200 tweets of a given screen name.
I am currently using a friend's screen name for testing.
"""
import os
import tweepy
import wget       # for downloading files
import textblob   # for sentiment analysis

# Import the keys from a module not added to Git. Cannot let these keys be publicly accessible.
from data_fetching.keys import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

TEST_SCREEN_NAME = 'Charlanardo'

DATA_SAVE_LOC = os.getcwd()+"\\data\\images-test\\"


# Create and authenticate an API object
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name=TEST_SCREEN_NAME,
                           count=200, include_rts=False,
                           exclude_replies=True)
media_files = set()
for tweet in tweets:
    media = tweet.entities.get('media', [])
    if len(media) > 0:
        media_files.add(media[0]['media_url'])

current_downloaded_files = os.listdir(DATA_SAVE_LOC)

for media_file in media_files:
    if media_file.split('/')[-1] in current_downloaded_files:
        print('File already downloaded: {}'.format(media_file.split('/')[-1]))
    else:
        wget.download(media_file, DATA_SAVE_LOC)

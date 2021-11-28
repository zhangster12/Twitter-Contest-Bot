'''Authorizes Twitter account use'''
import os
from dotenv import load_dotenv
import tweepy

load_dotenv('.env')

auth = tweepy.OAuthHandler(os.getenv('consumer_key'), os.getenv('consumer_secret'))
auth.set_access_token(os.getenv('access_token'), os.getenv('access_token_secret'))

# Controls Twitter account
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

my_screen_name = api.me().screen_name

'''Authorizes Twitter account use'''
from key import consumer_key, consumer_secret, access_token, access_token_secret
import os, tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

my_screen_name = api.me().screen_name
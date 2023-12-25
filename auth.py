'''Authorizes Twitter account use'''
from key import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account

# client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,
#                        access_token=access_token, access_token_secret=access_token_secret, wait_on_rate_limit=True)
api = tweepy.API(auth, wait_on_rate_limit = True)

my_screen_name = api.verify_credentials().screen_name
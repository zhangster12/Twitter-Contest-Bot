import tweepy
from tweepy.cursor import Cursor

consumer_key = 'Bi5Zzb6nl41grnJ1Xn1rxo4PY'
consumer_secret = 'cH2oLaZ67w44p1EIjsrp7uWXA0J6v9YHHMgGJKadkQBH35suBL'
access_token = '1198257732761128960-fPNjttTmjWEqVeHpiuw7I9uuCFCbtH'
access_token_secret = 'PsYjwInTECmlLQFc5SuIhyAdfS7WoX5dZoUZhcS25UHNl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

# Gets blocked users' screen names
blocked_screen_names = []
for blocked in tweepy.Cursor(api.blocks).items():
    blocked_screen_names.append(blocked.screen_name)

blocked_phrase = open('twitterFilter.txt', 'r').read().splitlines()
blocked_phrase_lower = [string.lower() for string in blocked_phrase]
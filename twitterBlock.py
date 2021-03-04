# Run with command: py twitterWinner.py
import os, time, tweepy
from tweepy.cursor import Cursor
from auth import api

os.system('cls')

# Gets blocked users' screen names
blocked_users = api.blocks()
blocked_screen_names = []
for user in blocked_users: 
    blocked_screen_names.append(user.screen_name)

# TwitterBot

for tweet in tweepy.Cursor(api.search, q = '#modi_job_do', lang = 'en', result_type = 'recent', tweet_mode = 'extended').items(100):

    # Check if it exists
    if not api.get_status(tweet.id):
        print('Status does not exist.\n\n----------\n')
        continue
    
    status = api.get_status(tweet.id)
    combined_tweet = tweet.user.name + ' -- @' + tweet.user.screen_name + ': \n' + tweet.full_text

    # Filter Tweets

    # Checks if user screen name is blocked
    if tweet.user.screen_name in blocked_screen_names:
        print(f'{tweet.user.screen_name} is blocked.\n\n----------\n')
        continue
    
    api.create_block(tweet.user.screen_name)
    print(f'{combined_tweet}\n\n----------\n')
    time.sleep(2.5)
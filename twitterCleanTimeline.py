import os, time, tweepy
from tweepy.cursor import Cursor
from auth import api

os.system('cls')

for tweet in tweepy.Cursor(api.user_timeline, tweet_mode = 'extended').items(3200):
    print(f'{tweet.user.name} - @{tweet.user.screen_name}:\n\n{tweet.full_text}\n\n----------\n') # Prints screen name and Tweet
    time.sleep(6)
    # tweet.destroy_favorite
    # tweet.unretweet()
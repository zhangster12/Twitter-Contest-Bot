import os, time, tweepy
from tweepy.cursor import Cursor
from auth import api

os.system('cls')

for tweet in tweepy.Cursor(api.user_timeline, tweet_mode = 'extended').items(3200):
    combined_tweet = tweet.user.name + ' -- @' + tweet.user.screen_name + ': ' + tweet.full_text
    print(f'{combined_tweet}\n\n----------\n')
    time.sleep(6)
    # tweet.destroy_favorite
    # tweet.unretweet()

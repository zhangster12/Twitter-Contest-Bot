import os, random, time, tweepy
from tweepy.cursor import Cursor
from auth import api
from datetime import datetime

os.system('cls')

now = datetime.utcnow()
start = now.replace(month = now.month - 1 if now.month > 1 else 12 - abs(now.month - 1))

for tweet in tweepy.Cursor(api.user_timeline, tweet_mode = 'extended').items(3200):
    
    status = api.get_status(tweet.id)
    original_status = api.get_status(status.retweeted_status.id)
    created_at = original_status.created_at

    # Checks if Tweet is in time interval
    if start < created_at < now:
        print(f'Date is in time interval: {created_at}\n')
        continue
    
    # Checks if Tweet is favorited
    if original_status.favorited == True:
        api.destroy_favorite(original_status.id)
        print('Tweet has been unfavorited.\n')
    
    # Not working
    # Checks if Tweet is Retweeted
    if original_status.retweeted == True or tweet.full_text.startswith('RT @'):
        api.unretweet(original_status.id)
        print('Tweet has been Unretweeted.\n')
    
    print(f'{created_at}:\n\n{tweet.full_text}\n') # Prints screen name and Tweet
    time.sleep(7.5)
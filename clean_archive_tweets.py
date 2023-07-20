from auth import api, my_screen_name
from datetime import datetime, timedelta
import os
import json
import random
import time
import tweepy

os.system('cls')

now = datetime.utcnow()
start = now - timedelta(days = 25)

f = open('tweets.json', encoding="utf8")
tweet_data = json.load(f)

for count, item in enumerate(tweet_data):
    tweet = item['tweet']
    id = tweet['id']
    
    try:
        status = api.get_status(id, tweet_mode = 'extended')
        created_at = status.created_at

        if start < created_at < now:
            continue

        if not hasattr(status, 'retweeted_status'):
            print(f'{count}. Tweet is not Retweet.\n')

            if created_at < start:
                api.destroy_status(status.id)
                print(f'{status.created_at}:\n\n{status.full_text}\n\nTweet has been deleted.\n')
                time.sleep(2.5)
            
            continue

        # If Tweet is favorited
        if status.favorited:
            api.destroy_favorite(status.id)
            print(f'{count}. Retweet has been unfavorited.\n')

        # If Tweet is Retweeted
        if status.retweeted or status.full_text.startswith('RT @'):
            api.destroy_status(status.id)
            print(f'{count}. Retweet has been Unretweeted.\n')
        
        time.sleep(2.5)
    
    except tweepy.TweepError as error:
        print(str(error) + '\n\n----------\n')
        continue


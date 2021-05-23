import os, time, tweepy
from tweepy.cursor import Cursor
from auth import api
from datetime import datetime, timedelta

os.system('cls')

# Get time interval
now = datetime.utcnow()
start = now - timedelta(days = 31)
print(f'Time Frame: {start} - {now}\n')

for tweet in tweepy.Cursor(api.user_timeline, tweet_mode = 'extended').items(3200):

    try:
        status = api.get_status(tweet.id)
        original_status = api.get_status(status.retweeted_status.id)
        created_at = original_status.created_at

        # Checks if Tweet is in time interval
        if start < created_at < now:
            print(f'Date is in time interval: {created_at}\n')
            continue
        
        # Checks if Tweet is favorited
        if status.favorited:
            api.destroy_favorite(status.id)
            print('Tweet has been unfavorited.\n')
        
        # Checks if Tweet is Retweeted
        if status.retweeted or tweet.full_text.startswith('RT @'):
            api.destroy_status(status.id)
            print('Tweet has been Unretweeted.\n')
        
        print(f'{created_at}:\n\n{tweet.full_text}\n') # Prints screen name and Tweet
        time.sleep(5)

    except AttributeError:
        print('Tweet is not Retweet.\n')
        continue

    except tweepy.TweepError as e:
        print(str(e) + '\n\n----------\n')
        continue
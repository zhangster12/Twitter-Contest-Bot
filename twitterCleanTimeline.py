from auth import api
from datetime import datetime, timedelta
import os, time, tweepy

os.system('cls')

# Get time interval
now = datetime.utcnow()
start = now - timedelta(days = 31)
print(f'Time Frame: {start} - {now}\n')

for count, tweet in enumerate(tweepy.Cursor(api.user_timeline, tweet_mode = 'extended').items(3200)):

    try:
        status = api.get_status(tweet.id)
        original_status = api.get_status(status.retweeted_status.id)
        created_at = original_status.created_at

        # Checks if Tweet is in time interval
        if start < created_at < now:
            print(f'{count}. Date is in time interval: {created_at}\n')
            continue
        
        # Checks if Tweet is favorited
        if status.favorited:
            api.destroy_favorite(status.id)
            print('{count}. Tweet has been unfavorited.\n')
        
        # Checks if Tweet is Retweeted
        if status.retweeted or tweet.full_text.startswith('RT @'):
            api.destroy_status(status.id)
            print('{count}. Tweet has been Unretweeted.\n')
        
        print(f'{created_at}:\n\n{tweet.full_text}\n') # Prints screen name and Tweet
        time.sleep(5)

    except AttributeError:
        print('Tweet is not Retweet.\n')
        status = api.get_status(tweet.id)
        created_at = status.created_at
        
        if created_at < start:
            api.destroy_status(status.id)
            print(f'{created_at}:\n\n{tweet.full_text}\n')
            print('Tweet has been deleted.\n')
        
        continue

    except tweepy.TweepError as e:
        print(str(e) + '\n\n----------\n')
        continue
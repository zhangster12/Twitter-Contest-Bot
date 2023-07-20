from auth import api
from datetime import datetime, timedelta
import os
import json
import time
import tweepy

os.system('cls')

api.destroy_status(1260022794944835587)

now = datetime.utcnow()
start = now - timedelta(days = 25)

f = open('like.json', encoding="utf8")
like_data = json.load(f)

for count, item in enumerate(like_data):
    like = item['like']
    id = like['tweetId']

    try:
        if hasattr(like, 'fullText'):

            if 'This Tweet is from a suspended account.' in like['fullText']:
                api.destroy_favorite(id)
                api.unretweet(id)
                print('Test')
                continue

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
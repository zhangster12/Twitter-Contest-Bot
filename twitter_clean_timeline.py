# Unfavorites, Unretweets, deletes Tweets from over a month ago

from auth import api
from datetime import datetime, timedelta
import os, time, tweepy

class cleanTimeline:

    @staticmethod
    def unfavorite_unretweet():

        # Get time interval
        now = datetime.utcnow()
        start = now - timedelta(days = 31)
        print(f'Time Frame: {start} - {now}\n')

        used = False

        for count, tweet in enumerate(tweepy.Cursor(api.user_timeline, screen_name = api.me().screen_name, exclude_replies = True, tweet_mode = 'extended').items(3200)):

            status = api.get_status(tweet.id, tweet_mode = 'extended')
            
            try:
                # If it's not a Retweet
                if not hasattr(status, 'retweeted_status'):
                    print(f'{count}. Tweet is not Retweet.\n')

                    if status.created_at < start:
                        api.destroy_status(status.id)
                        print(f'{status.created_at}:\n\n{status.full_text}\n\nTweet has been deleted.\n')

                    continue

                created_at = api.get_status(status.retweeted_status.id).created_at

                # If Tweet is in time interval
                if start < created_at < now:
                    print(f'{count}. Date is in time interval: {created_at}\n')
                    continue

                # If Tweet is favorited
                if status.favorited:
                    api.destroy_favorite(status.id)
                    print(f'{count}. Tweet has been unfavorited.\n')

                # If Tweet is Retweeted
                if status.retweeted or status.full_text.startswith('RT @'):
                    api.destroy_status(status.id)
                    print(f'{count}. Tweet has been Unretweeted.\n')

                print(f'{created_at}:\n\n{status.full_text}\n') # Prints screen name and Tweet
                used = True
                time.sleep(2.5)

            except tweepy.TweepError as e:
                print(str(e) + '\n\n----------\n')
                continue

        if used:
            cleanTimeline().unfavorite_unretweet()
'''Unfavorites, Unretweets, deletes Tweets from over a month ago'''
from auth import api, my_screen_name
from datetime import datetime, timedelta
from twitter_winner import get_list_lower, deemojify
import time, tweepy

def unfavorite_unretweet():
    '''Unfavorites, Unretweets, deletes Tweets from over a month ago'''

    blocked_phrase_lower = get_list_lower('twitterFilter.txt')

    # Get time interval
    now = datetime.utcnow()
    start = now - timedelta(days = 31)
    print(f'Time Frame: {start} - {now}\n')

    used = False

    for count, tweet in enumerate(tweepy.Cursor(api.user_timeline, screen_name = my_screen_name, exclude_replies = True, tweet_mode = 'extended').items(3200)):

        status = api.get_status(tweet.id, tweet_mode = 'extended')
        combined_tweet = deemojify(' '.join([status.user.name, status.user.screen_name, status.user.description, status .full_text]))

        try:
            # If it's not a Retweet
            if not hasattr(status, 'retweeted_status'):
                print(f'{count}. Tweet is not Retweet.\n')

                if status.created_at < start:
                    api.destroy_status(status.id)
                    print(f'{status.created_at}:\n\n{status.full_text}\n\nTweet has been deleted.\n')

                continue

            created_at = api.get_status(status.retweeted_status.id).created_at

            # If Tweet is in time interval and doesn't have blocked phrases
            if start < created_at < now and not any(p in combined_tweet.lower() for p in blocked_phrase_lower):
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

        except tweepy.TweepError as error:
            print(str(error) + '\n\n----------\n')
            continue

    if used:
        unfavorite_unretweet()
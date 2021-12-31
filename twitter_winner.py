'''Retweets, favorites, follows users to win contests'''
from auth import api
from datetime import datetime, timedelta
from twitter_filter import blocked_phrase_lower
import os, re, time, tweepy

def favorite_follow_retweet():
    '''Favorites, follows, Retweets'''

    now = datetime.utcnow()
    start = now - timedelta(days = 31)

    # Search filters and number
    search_terms = ' OR '.join(['retweet to win', '#retweettowin', '#giveaway'])
    filters = ' AND '.join(['-attempt', '-buy', '-caption', '-click', '-comment', '-comments' '-confirm', '-donate', '-download', '-fill',
        '-form', '-guess', '-help', '-join', '-link', '-pinned', '-poll', '-post', '-predict', '-quote', '-refer', '-register', '-reply',
        '-screenshot', '-send', '-share', '-spread', '-sub', '-submit', '-subscribe', '-vote', '-votes'
        '-filter:quote', '-filter:replies', '-filter:retweets'])

    query = search_terms + ' ' + filters # Cannot exceed 500 characters

    try:
        # Blocked users' screen names
        blocked_id = [b.id for b in tweepy.Cursor(api.blocks).items()]

        os.system('cls')

        # TwitterBot

        for count, tweet in enumerate(tweepy.Cursor(api.search, q = query, lang = 'en', result_type = 'recent', tweet_mode = 'extended').items(1000)):

            try:
                status = api.get_status(tweet.id, tweet_mode = 'extended')
                combined_tweet = deemojify(' '.join([tweet.user.name, tweet.user.screen_name, tweet.user.description, tweet.full_text]))

                # User screen name is blocked
                if tweet.user.id in blocked_id:
                    print(f'{count}. {tweet.user.screen_name} is blocked.\n\n----------\n')
                    continue

                # Tweet contains blocked phrases
                if any(p in combined_tweet.lower() for p in blocked_phrase_lower):
                    print(f'{count}. Tweet contains blocked phrases.\n\n----------\n')
                    continue

                # User doesn't have enough followers, follower/following count isn't doesn't have profile pic, description, recently created
                if tweet.user.followers_count < 100 or tweet.user.followers_count/tweet.user.friends_count < 1 or tweet.user.friends_count == 0 or status.user.default_profile_image or not tweet.user.description or start < status.user.created_at < now:
                    print(f'{count}. {tweet.user.screen_name} does not have enough followers, is default, has no description, too recent.\n\n----------\n')
                    continue

                # Tweet contains sensitive media
                if hasattr(tweet, 'possibly_sensitive') and tweet.possibly_sensitive:
                    print(f'{count}. Tweet contains sensitive media.\n\n----------\n')
                    continue

                # Tweet has already been favorited or Retweeted
                if status.favorited or status.retweeted:
                    print(f'{count}. Tweet has already been favorited or Retweeted.\n\n----------\n')
                    api.create_friendship(tweet.user.screen_name)
                    continue

                api.create_friendship(tweet.user.id) # Follows Tweet's user screen name

                for user in status.entities['user_mentions']: # Follows all user mentions
                    api.create_friendship(user['id'])

                tweet.favorite() # Favorites the Tweet
                tweet.retweet() # Retweets the Tweet
                print(deemojify(f'{count}. {tweet.user.name} - @{tweet.user.screen_name}:\n\n{tweet.full_text}\n\n----------\n')) # Prints screen name and Tweet
                time.sleep(2.5)

            except tweepy.TweepError as error:
                print(f'{count}. {str(error)}\n\n----------\n')
                continue

            # except ZeroDivisionError as error:
            #     print(f'{count}. {str(error)}\n\n----------\n')
            #     continue

    except tweepy.TweepError as error:
        print(str(error) + '\n')

def deemojify(text):
    '''Returns a string without emojis'''
    regrex_pattern = re.compile('['
        u'\U0001F600-\U0001F64F' # Emoticons
        u'\U0001F300-\U0001F5FF' # Symbols and pictographs
        u'\U0001F680-\U0001F6FF' # Transport and map symbols
        u'\U0001F1E0-\U0001F1FF' # Flags (iOS)
        u'\U0001F1F2-\U0001F1F4' # Macau flag
        u'\U0001F1E6-\U0001F1FF' # Flags
        u'\U0001F600-\U0001F64F'
        u'\U00002702-\U000027B0'
        u'\U000024C2-\U0001F251'
        u'\U0001f926-\U0001f937'
        u'\U0001F1F2'
        u'\U0001F1F4'
        u'\U0001F620'
        u'\u200d'
        u'\u2640-\u2642'
        ']+', flags = re.UNICODE)

    return regrex_pattern.sub(r'', text)
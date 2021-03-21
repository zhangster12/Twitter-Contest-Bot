# Run with command: py twitterWinner.py
import os, time, tweepy
from tweepy.cursor import Cursor
from auth import api, blocked_screen_names, blocked_phrase_lower

os.system('cls')

print(blocked_phrase_lower)

# Search filters and number
search_terms = ' OR '.join(["retweet to win", '#retweettowin'])
filters = ' AND '.join(['-filter:retweets', '-filter:replies', '-filter:quote', '-filter:nullcast'])

query = search_terms + ' ' + filters

# TwitterBot

for tweet in tweepy.Cursor(api.search, q = query, lang = 'en', result_type = 'recent', tweet_mode = 'extended').items(100):

    # Check if it exists
    if not api.get_status(tweet.id):
        print('Status does not exist.\n\n----------\n')
        continue
    
    status = api.get_status(tweet.id)
    combined_tweet = tweet.user.name + tweet.user.screen_name + tweet.user.description + tweet.full_text

    # Filter Tweets

    # Checks if user screen name is blocked
    if tweet.user.screen_name in blocked_screen_names:
        print(f'{tweet.user.screen_name} is blocked.\n\n----------\n')
        continue

    # Checks if Tweet contains blocked phrases
    elif any(phrase in combined_tweet.lower() for phrase in blocked_phrase_lower):
        api.create_block(tweet.user.screen_name)
        print(f'Tweet contains blocked phrases.\n{tweet.user.screen_name} has been blocked.\n\n----------\n')
        continue

    # Checks if Tweet has already been favorited or Retweeted
    elif status.favorited == True or status.retweeted == True:
        print('Tweet has already been favorited or Retweeted.\n\n----------\n')
        api.create_friendship(tweet.user.screen_name)
        continue

    api.create_friendship(tweet.user.screen_name) # Follows tweet's user screen name
    tweet.favorite() # Favorites the Tweet
    tweet.retweet() # Retweets the Tweet
    print(f'{tweet.user.name} - @{tweet.user.screen_name}:\n\n{tweet.full_text}\n\n----------\n') # Prints screen name and Tweet
    time.sleep(7.5)
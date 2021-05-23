# Run with command: py twitterWinner.py
import os, time, tweepy
from tweepy.cursor import Cursor
from auth import api

os.system('cls')

# Blocked phrases
blocked_phrase = open('twitterFilter.txt', 'r').read().splitlines()
blocked_phrase_lower = [string.lower() for string in blocked_phrase]

# Blocked users' screen names
blocked_screen_names = []
for blocked in tweepy.Cursor(api.blocks).items():
    blocked_screen_names.append(blocked.screen_name)

# Search filters and number
search_terms = ' OR '.join(["retweet to win", '#retweettowin'])
filters = ' AND '.join(['-comment', '-comments', '-tag', '-reply', '-filter:retweets', '-filter:replies', '-filter:quote', '-filter:nullcast'])

query = search_terms + ' ' + filters

# TwitterBot
for tweet in tweepy.Cursor(api.search, q = query, lang = 'en', result_type = 'recent', tweet_mode = 'extended').items(200):

    try:
        status = api.get_status(tweet.id)
        combined_tweet = tweet.user.name + tweet.user.screen_name + tweet.user.description + tweet.full_text

        # Filter Tweets

        # User screen name is blocked
        if tweet.user.screen_name in blocked_screen_names:
            print(f'{tweet.user.screen_name} is blocked.\n\n----------\n')
            continue

        # Tweet contains blocked phrases
        elif any(phrase in combined_tweet.lower() for phrase in blocked_phrase_lower):
            api.create_block(tweet.user.screen_name)
            print(f'Tweet contains blocked phrases.\n{tweet.user.screen_name} has been blocked.\n\n----------\n')
            continue

        # Tweet has already been favorited or Retweeted
        elif status.favorited or status.retweeted:
            print('Tweet has already been favorited or Retweeted.\n\n----------\n')
            api.create_friendship(tweet.user.screen_name)
            continue

        api.create_friendship(tweet.user.screen_name) # Follows tweet's user screen name
        tweet.favorite() # Favorites the Tweet
        tweet.retweet() # Retweets the Tweet
        print(f'{tweet.user.name} - @{tweet.user.screen_name}:\n\n{tweet.full_text}\n\n----------\n') # Prints screen name and Tweet
        time.sleep(5)

    except tweepy.TweepError as e:
        print(str(e) + '\n\n----------\n')
        continue

# Sorts twitterFilter.txt alphabetically
blocked_phrase = list(set(blocked_phrase))
blocked_phrase.sort(key = str.casefold)
sorted_file = open('twitterFilter.txt', 'w')

for i, phrase in enumerate(blocked_phrase):
    sorted_file.writelines(phrase)
    if i == len(blocked_phrase) - 1:
        break
    else:
        sorted_file.writelines('\n')
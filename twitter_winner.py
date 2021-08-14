from auth import api
from datetime import datetime, timedelta
import re, os, time, tweepy

class winner:
    
    def favorite_follow_retweet(self):
        blocked_phrase_lower = self.get_list_lower('twitterFilter.txt')
        
        now = datetime.utcnow()
        start = now - timedelta(days = 31)

        # Search filters and number
        search_terms = ' OR '.join(['retweet to win', '#retweettowin', '#giveaway'])
        filters = ' AND '.join(['-attempt', '-buy', '-caption', '-click', '-comment', '-comments' '-confirm', '-donate', '-download', '-fill',
            '-form', '-guess', '-help', '-join', '-link', '-pinned', '-poll', '-post', '-predict', '-quote', '-refer', '-register', '-reply',
            '-screenshot', '-send', '-share', '-spread', '-sub', '-submit', '-subscribe', '-vote',
            '-filter:quote', '-filter:replies', '-filter:retweets'])

        # Cannot exceed 500 characters
        query = search_terms + ' ' + filters
        print(len(query))

        try:
            # Blocked users' screen names
            blocked_id = [b.id for b in tweepy.Cursor(api.blocks).items()]

            os.system('cls')

            # TwitterBot

            for count, tweet in enumerate(tweepy.Cursor(api.search, q = query, lang = 'en', result_type = 'recent', tweet_mode = 'extended').items(500)):

                try:
                    status = api.get_status(tweet.id, tweet_mode = 'extended')
                    combined_tweet = self.deEmojify(' '.join([tweet.user.name, tweet.user.screen_name, tweet.user.description, tweet.full_text]))

                    # User screen name is blocked
                    if tweet.user.id in blocked_id:
                        print(f'{count}. {tweet.user.screen_name} is blocked.\n\n----------\n')
                        continue

                    # Tweet contains blocked phrases
                    elif any(p in combined_tweet.lower() for p in blocked_phrase_lower):
                        print(f'{count}. Tweet contains blocked phrases.\n\n----------\n')
                        continue
                    
                    # User doesn't have enough followers
                    elif tweet.user.followers_count < 100 or tweet.user.followers_count/tweet.user.friends_count < 1 or status.user.default_profile_image or not tweet.user.description or start < status.user.created_at < now:
                        print(f'{count}. {tweet.user.screen_name} does not have enough followers, is default, has no description, too recent.\n\n----------\n')
                        continue
                    
                    # Tweet contains sensitive media
                    elif hasattr(tweet, 'possibly_sensitive') and tweet.possibly_sensitive:
                        print(f'{count}. Tweet contains sensitive media.\n\n----------\n')
                        continue

                    # Tweet has already been favorited or Retweeted
                    elif status.favorited or status.retweeted:
                        print(f'{count}. Tweet has already been favorited or Retweeted.\n\n----------\n')
                        api.create_friendship(tweet.user.screen_name)
                        continue

                    api.create_friendship(tweet.user.id) # Follows Tweet's user screen name
                    
                    for user in status.entities['user_mentions']: # Follows all user mentions
                        api.create_friendship(user['id'])
                    
                    tweet.favorite() # Favorites the Tweet
                    tweet.retweet() # Retweets the Tweet
                    print(self.deEmojify(f'{count}. {tweet.user.name} - @{tweet.user.screen_name}:\n\n{tweet.full_text}\n\n----------\n')) # Prints screen name and Tweet
                    time.sleep(2.5)

                except tweepy.TweepError as e:
                    print(f'{count}. {str(e)}\n\n----------\n')
                    continue
                
                except ZeroDivisionError as e:
                    print(f'{count}. {str(e)}\n\n----------\n')
                    continue
    
        except tweepy.TweepError as e:
            print(str(e) + '\n')

    # Sorts a .txt file alphabetically
    @staticmethod
    def sort_file(file):
        file_list = open(file, 'r', encoding = 'utf-8', errors = 'ignore').read().splitlines()
        file_list = list(set(file_list)) # Gets rid of duplicates
        file_list.sort(key = str.casefold) # Sorts alphabetically

        with open(file, 'w') as f:
            f.write('\n'.join(file_list))
        
        return file + ' is sorted.'
    
    # Returns a lowercase list
    @staticmethod
    def get_list_lower(file):
        list = open(file, 'r', encoding = 'utf-8', errors = 'ignore').read().splitlines()
        list = [string.lower() for string in list] # Makes all items lowercase
        return list
    
    # Returns a string without emojis
    @staticmethod
    def deEmojify(text):
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
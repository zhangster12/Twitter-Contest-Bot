from auth import api
import os, time, tweepy

class winner:
    
    def favorite_follow_retweet(self):
        
        blocked_phrase_lower = self.get_list_lower('twitterFilter.txt')

        # Blocked users' screen names
        blocked_screen_names = [b.screen_name for b in tweepy.Cursor(api.blocks).items()]

        # Search filters and number
        search_terms = ' OR '.join(['retweet to win', '#retweettowin'])
        filters = ' AND '.join(['-attempt', '-comment', '-comments', '-guess', '-help', '-join', '-poll', '-post', '-predict', '-refer',
            '-register', '-reply', '-screenshot', '-share', '-spread', '-submit', '-subscribe', '-tag', '-tell', '-vote', '-voting',
             '-filter:quote', '-filter:replies', '-filter:retweets'])

        query = search_terms + ' ' + filters

        os.system('cls')

        # TwitterBot
        for count, tweet in enumerate(tweepy.Cursor(api.search, q = query, lang = 'en', result_type = 'recent', tweet_mode = 'extended').items(500)):

            try:
                status = api.get_status(tweet.id)
                combined_tweet = tweet.user.name + tweet.user.screen_name + tweet.user.description + tweet.full_text

                # User screen name is blocked
                if tweet.user.screen_name in blocked_screen_names:
                    print(f'{count}. {tweet.user.screen_name} is blocked.\n\n----------\n')
                    continue

                # Tweet contains blocked phrases
                elif any(phrase in combined_tweet.lower() for phrase in blocked_phrase_lower):
                    print(f'{count}. Tweet contains blocked phrases.\n\n----------\n')
                    #api.create_block(tweet.user.screen_name)
                    #print(f'{count}. Tweet contains blocked phrases.\n{tweet.user.screen_name} has been blocked.\n\n----------\n')
                    continue

                # Tweet has already been favorited or Retweeted
                elif status.favorited or status.retweeted:
                    print(f'{count}. Tweet has already been favorited or Retweeted.\n\n----------\n')
                    api.create_friendship(tweet.user.screen_name)
                    continue

                api.create_friendship(tweet.user.screen_name) # Follows tweet's user screen name
                tweet.favorite() # Favorites the Tweet
                tweet.retweet() # Retweets the Tweet
                print(f'{count}. {tweet.user.name} - @{tweet.user.screen_name}:\n\n{tweet.full_text}\n\n----------\n') # Prints screen name and Tweet
                time.sleep(3)

            except tweepy.TweepError as e:
                print(str(e) + '\n\n----------\n')
                continue
    
    @staticmethod
    def sort_file(file):
        file_list = open(file, 'r').read().splitlines()
        file_list = list(set(file_list)) # Gets rid of duplicates
        file_list.sort(key = str.casefold) # Sorts alphabetically

        with open(file, 'w') as f:
            f.write('\n'.join(file_list))
        
        return file + ' is sorted.'
    
    @staticmethod
    def get_list_lower(file):
        list = open(file, 'r').read().splitlines()
        list = [string.lower() for string in list] # Makes all items lowercase
        return list
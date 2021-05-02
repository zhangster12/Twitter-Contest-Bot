# Randomly unfollows users if the authenticating user's following number is greater than 2000 until it's 1500

import os, random, time, tweepy
from tweepy.cursor import Cursor
from auth import api

os.system('cls')

following_count = api.me().friends_count
my_screen_name = api.me().screen_name

if following_count > 2000:
    print(f'Current following count is at {following_count}.')
    for friend in tweepy.Cursor(api.friends).items(following_count):
        
        # Checks if user is following authenticating user
        status = api.show_friendship(source_screen_name = friend.screen_name, target_screen_name = my_screen_name)
        if status[0].following:
            print(f'{friend.screen_name} follows {my_screen_name}.')
            continue
        
        # Randomly skips users
        elif random.randint(0, 2) == 1:
            print('User has been skipped.')
            continue
        
        # Ends loop if following count is 1500
        elif api.me().friends_count == 1500:
            break
        
        else:
            api.destroy_friendship(friend.screen_name)
            print(f'{friend.screen_name} has been unfollowed.')
            time.sleep(5)
else:
    print(f'Following count is at {following_count}. No unfollowing needed.')
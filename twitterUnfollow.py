import os, time, tweepy
from tweepy.cursor import Cursor
from auth import api

os.system('cls')

following_count = api.me().friends_count

if following_count > 2000:
    print(f'Current following count is at {following_count}.')
    for friend in tweepy.Cursor(api.friends).items(following_count - 1000): 
        print(friend.screen_name)
        api.destroy_friendship(friend.screen_name)
        time.sleep(6)
else:
    print(f'Following count is at {following_count}. No unfollowing needed.')
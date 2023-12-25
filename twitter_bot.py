'''Main file for Twitter bot'''
from auth import api, my_screen_name
from datetime import datetime
from twitter_clean_timeline import unfavorite_unretweet
from twitter_unfollow import unfollow
from twitter_winner import favorite_follow_retweet
import os, time

os.system('cls')
day = datetime.today().day

print('Twitter Bot for ' + my_screen_name + '\n')

try:
    # Run script
    if day == 1 or api.verify_credentials().friends_count > 2500:
        unfollow()
        unfavorite_unretweet()
    elif day in [5, 10, 15, 20, 25, 30] or api.verify_credentials().favourites_count > 2500 or api.verify_credentials().statuses_count > 2500:
        unfavorite_unretweet()
    else:
        favorite_follow_retweet()
except KeyboardInterrupt:
    pass

input('Enter to continue.\n')
print('Goodbye!\n')
time.sleep(2.5)
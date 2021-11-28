'''Main file for Twitter bot'''
# Import statements
import os
import time
from datetime import datetime

from auth import api, my_screen_name
from twitter_clean_timeline import unfavorite_unretweet
from twitter_unfollow import Unfollow
from twitter_winner import Winner

# Create class instance
win = Winner
unfollow = Unfollow()

os.system('cls')
day = datetime.today().day

print('Twitter Bot for ' + my_screen_name + '\n\n' + win.sort_file('twitterFilter.txt') + '\n')

# Run script
if day == 1 or api.me().friends_count > 3000:
    unfollow.unfollow()
elif day in [5, 10, 15, 20, 25, 30] or api.me().favourites_count > 5000 or api.me().statuses_count > 5000:
    unfavorite_unretweet()
else:
    win.favorite_follow_retweet()

input('Enter to continue.\n')
print('Goodbye!\n')
time.sleep(5)

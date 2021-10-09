from auth import api
from datetime import datetime
from twitter_clean_timeline import cleanTimeline
from twitter_unfollow import unfollow
from twitter_winner import winner
import os, time

# Create class instance
win = winner()
unfollow = unfollow()
clean_timeline = cleanTimeline()

os.system('cls')
day = datetime.today().day

print('Twitter Bot for ' + api.me().screen_name + '\n')
print(win.sort_file('twitterFilter.txt') + '\n')

# Run script
if day == 1 or api.me().friends_count > 3000:
    unfollow.unfollow()
elif day in [7, 14, 21, 28] or api.me().favourites_count > 4000 or api.me().statuses_count > 4000 or api.me().favourites_count + api.me().statuses_count > 5000:
    clean_timeline.unfavorite_unretweet()
else:
    win.favorite_follow_retweet()

input('Enter to continue.\n')

print('Goodbye!')
time.sleep(5)
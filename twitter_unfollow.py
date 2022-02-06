'''Randomly unfollows users if the authenticating user's following number is greater than 2000 until it's 1500'''
from auth import api, my_screen_name
import random, time, tweepy

def unfollow():
    '''Unfollows users'''

    print(f'Current following count is at {api.me().friends_count}.')
    for count, friend in enumerate(tweepy.Cursor(api.friends).items(api.me().friends_count)):

        if count <= 500:
            print(f'{count}. User was recently followed.' )
            continue

        # Checks if user is following authenticating user
        if following_me(friend.screen_name):
            print(f'{count}. {friend.screen_name} follows {my_screen_name}.')
            continue

        # Randomly skips users
        if random.randint(0, 1) == 1:
            print(f'{count}. User has been skipped.')
            continue

        # Ends if following count is 1500
        if api.me().friends_count == 1500:
            break

        api.destroy_friendship(friend.screen_name)
        print(f'{count}. {friend.screen_name} has been unfollowed.')
        time.sleep(2.5)

def following_me(screen_name):
    '''Checks if a user is following the authenticating user'''

    status = api.show_friendship(source_screen_name = screen_name, target_screen_name = my_screen_name)
    return status[0].following
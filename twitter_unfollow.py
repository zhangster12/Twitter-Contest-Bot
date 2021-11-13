# Randomly unfollows users if the authenticating user's following number is greater than 2000 until it's 1500

from auth import api, my_screen_name
import random, time, tweepy

class unfollow:

    def unfollow(self):
        
        if api.me().friends_count > 1500:
            print(f'Current following count is at {api.me().friends_count}.')
            for count, friend in enumerate(tweepy.Cursor(api.friends).items(api.me().friends_count)):

                if count <= 500:
                    print(f'{count}. User was recently followed.' )
                    continue

                # Checks if user is following authenticating user
                if self.following_me(friend.screen_name):
                    print(f'{count}. {friend.screen_name} follows {my_screen_name}.')
                    continue

                # Randomly skips users
                elif random.randint(0, 1) == 1:
                    print(f'{count}. User has been skipped.')
                    continue

                # Ends if following count is 1500
                elif api.me().friends_count == 1500:
                    break

                else:
                    api.destroy_friendship(friend.screen_name)
                    print(f'{count}. {friend.screen_name} has been unfollowed.')
                    time.sleep(2.5)
        else:
            print(f'Following count is at {api.me().friends_count}. No unfollowing needed.\n')

    # Checks if a user is following the authenticating user
    def following_me(self, screen_name):
        status = api.show_friendship(source_screen_name = screen_name, target_screen_name = my_screen_name)
        return status[0].following
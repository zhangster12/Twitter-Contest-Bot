# Randomly unfollows users if the authenticating user's following number is greater than 2000 until it's 1500

from auth import api
import random, time, tweepy

class unfollow:
    my_screen_name = api.me().screen_name

    def unfollow(self):

        if api.me().friends_count > 2000:
            print(f'Current following count is at {api.me().friends_count}.')
            for count, friend in enumerate(tweepy.Cursor(api.friends).items(api.me().friends_count)):
                
                if count <= 500:
                    print(f'{count}. User was recently followed.' )
                    continue
                
                # Checks if user is following authenticating user
                elif self.following_me(friend.screen_name):
                    print(f'{count}. {friend.screen_name} follows {self.my_screen_name}.')
                    continue
                
                # Randomly skips users
                elif random.randint(0, 2) == 1:
                    print(f'{count}. User has been skipped.')
                    continue
                
                # Ends loop if following count is 1500
                elif api.me().friends_count == 1500:
                    break
                
                else:
                    api.destroy_friendship(friend.screen_name)
                    print(f'{count}. {friend.screen_name} has been unfollowed.')
                    time.sleep(3)
        else:
            print(f'Following count is at {api.me().friends_count}. No unfollowing needed.')
    
    def following_me(self, screen_name):
        status = api.show_friendship(source_screen_name = screen_name, target_screen_name = self.my_screen_name)
        return status[0].following
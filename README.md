# Twitter-Contest-Bot
Twitter-Contest-Bot is a bot for automating Retweeting and liking Twitter contests to win free prizes.

## Getting Started
Install Tweepy and create `twitterFilter.txt`.

### Prerequisites
```
npm install dotenv
npm install tweepy
```

## Usage
Only accept the reward if it's completely free, no shipping, joining.
Use English in `twitterFilter.txt`.

### Run bot:
```
py twitter_bot.py
```

### Push updates to GitHub:
```
py get_list.py
git add .
git commit -m 'Edited file'
git push origin
pyinstaller --noconfirm --onedir --console --icon 'twitter-bot.ico'  'twitter_bot.py'
del 'build'

```

## Roadmap
- [ ] Block polls
- [ ] Fix user timeline Tweet limit

## Contact
Project Link: [https://github.com/zhangster12/Twitter-Contest-Bot](https://github.com/zhangster12/Twitter-Contest-Bot)
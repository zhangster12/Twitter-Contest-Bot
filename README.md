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

### Create executable:
```
pyinstaller --noconfirm --onedir --console --icon 'C:/Users/dyzha/Documents/Projects/Twitter/twitter-bot.ico'  'C:/Users/dyzha/Documents/Projects/Twitter/twitter_bot.py'
```

### Push updates to GitHub:
```
git add .
git commit -m 'Edited file'
git push origin
```

## Roadmap
- [ ] Block polls
- [ ] Fix user timeline Tweet limit

## Contact
Project Link: [https://github.com/zhangster12/Twitter-Contest-Bot](https://github.com/zhangster12/Twitter-Contest-Bot)
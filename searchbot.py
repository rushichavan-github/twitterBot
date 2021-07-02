import tweepy
import time

consumer_key = 'zrgz8HNXV5Ltyd2hhtQaz0cZn'
consumer_secret = 'oXZ6lXqjf0MgTuc7dgggVOOWANNFZwnSd9cbh9qJfrsKyEaVDe'
key = '1304621202237919234-xMphi4yTRdhKSeYcgVwBJn7r2aoC9g'
secret = 'opO5wloSnjk6RWozvYhzFWqNqrbHsIrTr2wepCY4Fpsi0'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "100daysofcode"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()
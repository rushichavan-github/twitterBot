import tweepy
import time

consumer_key = 'zrgz8HNXV5Ltyd2hhtQaz0cZn'
consumer_secret = 'oXZ6lXqjf0MgTuc7dgggVOOWANNFZwnSd9cbh9qJfrsKyEaVDe'
key = '1304621202237919234-xMphi4yTRdhKSeYcgVwBJn7r2aoC9g'
secret = 'opO5wloSnjk6RWozvYhzFWqNqrbHsIrTr2wepCY4Fpsi0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("Replied To ID - " + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + " Good Luck For #YourFuture!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(30)

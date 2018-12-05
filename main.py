import tweepy
import json

auth = ""
with open("auth.json") as f:
    jsnf = json.load(f)
    auth = tweepy.OAuthHandler(jsnf['api_key'], jsnf['api_secret_key'])
    auth.set_access_token(jsnf['token'], jsnf['secret_token'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

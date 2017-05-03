#!/usr/bin/env python
import tweepy
# from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twts = api.search(q="my name is 503.")

# list of specific strings we want to check for in Tweets
t = ['my name is 503.']

for s in twts:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hello!" % (sn)
            s = api.update_status(m, s.id)
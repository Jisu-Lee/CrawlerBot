import tweepy
import random
import sys
import datetime
import os
from keys import keys

API_KEY = keys['consumer_key']
API_SECRET = keys['consumer_secret']
ACCESS_KEY = keys['access_token']
ACCESS_SECRET = keys['access_token_secret']

oAuth = tweepy.OAuthHandler(API_KEY, API_SECRET)
oAuth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth_handler=oAuth)

userID = random.randrange(1,99999999)
print(userID)
numTweet = 20
#numUser = 1
today = datetime.datetime.today()

try:
    user = api.get_user(userID)
except tweepy.error.TweepError as e:
    user = None
    print(e)
if user != None:
    print(user.name)
    try:
        timeline = api.user_timeline(userID, count = 20)
        for tweet in timeline:
            print(tweet.text)
    except tweepy.error.TweepError as e:
        timeline = None
        print(e)
    if timeline != None :
        if not os.path.exists("rs"):
            os.makedirs("rs")
        if not os.path.exists("rs/tweets"):
            os.makedirs("rs/tweets")
        ofName = "rs/tweets/"     #(user_name)_(mmddyy).txt
        ofName += user.name
        ofName += "_"
        ofName += ("0" + str(today.month)) if (today.month < 10) else str(today.month)
        ofName += ("0" + str(today.day)) if (today.day < 10) else str(today.day)
        ofName += str(today.year)[-2] + str(today.year)[-1]
        ofName += ".txt"
        print(ofName)
        of = open(ofName,'w')
        for tweet in timeline:
            wstr = ""       #date : mmddyy content : (tweet) id : (status id)
            wstr += "date : "
            tweetday = ""      #mmddyy
            tweetday += ("0" + str(tweet.created_at.month)) if (tweet.created_at.month < 10) else str(tweet.created_at.month)
            tweetday += ("0" + str(tweet.created_at.day)) if (tweet.created_at.day < 10) else str(tweet.created_at.day)
            tweetday += str(tweet.created_at.year)[-2] + str(tweet.created_at.year)[-1]
            print(tweetday)
            wstr += tweetday
            wstr += " content : " + tweet.text
            wstr += " id : " + tweet.id_str
            print(wstr)
            of.write(wstr + "\n")


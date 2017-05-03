import tweepy
import random

API_KEY = "7Uiv7Nh4cgEiHkGBjpK1ZBSM8"
API_SECRET = "VUEkxczxXyl3bhBMPTo1HIWYX9RLY50LrSa6oFgSUjHuOzdEcA"
ACCESS_KEY = "859611207883309056-Xj0izu3bgSA9IvETl1yAndrwXmUHWY5"
ACCESS_SECRET = "wCkjOdtMGTgL00EVKyrzXX3NTImicPY6gKKdGtub8BZcw"

oAuth = tweepy.OAuthHandler(API_KEY, API_SECRET)
oAuth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth_handler=oAuth)

userID = random.randrange(1,99999999)
try:
    user = api.get_user(userID)
except tweepy.error.TweepError as e:
    user = None
    print(e)
if user != None:
    print(user.name)
    try:
        timeline = api.user_timeline(userID)
        for tweet in timeline:
            print(tweet.text)
    except tweepy.error.TweepError as e:
        print(e)
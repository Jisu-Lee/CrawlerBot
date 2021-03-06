#!\usr\bin\env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from keys import keys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
	api.update_status(line)
	time.sleep(10)#Tweet every 15 minutes
	

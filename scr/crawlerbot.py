#!\usr\bin\env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '7Uiv7Nh4cgEiHkGBjpK1ZBSM8'
CONSUMER_SECRET = 'VUEkxczxXyl3bhBMPTo1HIWYX9RLY50LrSa6oFgSUjHuOzdEcA'
ACCESS_KEY = '859611207883309056-Xj0izu3bgSA9IvETl1yAndrwXmUHWY5'
ACCESS_SECRET = 'wCkjOdtMGTgL00EVKyrzXX3NTImicPY6gKKdGtub8BZcw'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
	api.update_status(line)
	time.sleep(900)#Tweet every 15 minutes
	

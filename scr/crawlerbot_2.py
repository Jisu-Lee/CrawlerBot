#!\usr\bin\env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'PEHHVYmOmvAa7A4vRPHjPWTsW'
CONSUMER_SECRET = 'UR4prH7U1VBwk89CZJUQ1nx2fhecd2U4HEtRwnfcV37SEUADqS'
ACCESS_KEY = '859639962857340928-NXovfyQhuEOIJremJEiJmBO9EPWsI2K'
ACCESS_SECRET = '9HqNi7r9dxo8N2t6ekF6jBEEdA1AXONeTyX7grKDpMeNF'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(10)  # Tweet every 15 minutes


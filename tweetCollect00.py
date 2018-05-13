# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:42:25 2018

@author: Edouard
"""

import tweepy #library tweepy
import csv #open a .csv file

c = csv.writer(open("TweetsCollected.csv", "wb"))

consumer_key =  "" #Write between the "" your consumer key
consumer_secret = "" #Write between the "" your consumer secret key

access_token = "" #Write between the "" your acess token
access_token_secret = "" #Write between the "" your acess token

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    #print tweet.text    
    tweets = tweet.text.encode('ascii', 'ignore').decode('ascii')
    c.writerow([tweets])

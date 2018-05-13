import tweepy
from tweepy import OAuthHandler

consumer_key = 'iq1QBVUO4qPUwFvOeZi0j3VyB'
consumer_secret = 'rbj4wBQw92Q00Sy77PJt7EobtlPReJYCzTOjwgC7ZAQxm9TAy8'
access_token = '944258736-ZhlyGXUfYoS7Y8rwIBdvba5pkmJaAjNMlSwa6urg'
access_secret = 'mg3K57PSSvzpgg1efkEIagxlYu57RTf50nOFftFjq6p6N'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for tweet_info in tweepy.Cursor(api.search, q="Trump", lang = "fr", tweet_mode="extended").items(100):
    if 'retweeted_status' in dir(tweet_info):
        tweet=tweet_info.retweeted_status.full_text
    else:
        tweet=tweet_info.full_text
    print("--------------------")
    print(tweet)
    print("--------------------\n")
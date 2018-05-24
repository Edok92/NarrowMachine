import tweepy
from tweepy import OAuthHandler

def get_tweets(mot_cle, nombre):
    tweets = []
    consumer_key = 'SUYaXWTGvYr8wmkX1JUhqh95y'
    consumer_secret = 'WR8YHxD5jCUPoJD5KbaUMVPyzImKC4i4BFK3Z4jvJMRhYzhXfT'
    access_token = '2225613595-yiVTf68PQFXn9RuOFDIKoZRSfunZcX82SGIftsh'
    access_secret = 'pG0z5Cx62EffbgwHHAGHzuAjaA6FsQDc6mMEXgPr92BhB'
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    api = tweepy.API(auth)
    
    for tweet_info in tweepy.Cursor(api.search, q=mot_cle, lang = "fr", tweet_mode="extended").items(nombre):
        if 'retweeted_status' in dir(tweet_info):
            tweet=tweet_info.retweeted_status.full_text
        else:
            tweet=tweet_info.full_text        
        tweets.append(tweet)
        
    return tweets
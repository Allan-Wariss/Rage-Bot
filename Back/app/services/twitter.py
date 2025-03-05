import tweepy
from app.config import settings

class TwitterClient:
    def __init__(self):
        self.auth = tweepy.OAuth1UserHandler(
            consumer_key=settings.TWITTER_API_KEY,
            consumer_secret=settings.TWITTER_API_SECRET,
            access_token=settings.TWITTER_ACCESS_TOKEN,
            access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET
        )
        
    def get_client(self):
        return tweepy.API(self.auth)
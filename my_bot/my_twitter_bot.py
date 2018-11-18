import time
import tweepy
from keys import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id) + ' - ' + mention.text)
    if '@canozgurparlak' in mention.text.lower():
        print('found @canozgurparlak')

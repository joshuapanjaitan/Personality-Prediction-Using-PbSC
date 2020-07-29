import tweepy
from textblob import TextBlob
import numpy as np
import csv
import datetime
import detectlanguage

spam = ['automatically checked by', 'KkRY0Y',
        'Today stats']  # special bot char

# API key for detecting language
detectlanguage.configuration.api_key = "02cc20e17ba6505343bacbfbbc1252f5"

consumer_key = 'Z46tloZwrCEXOd4FlYdoBMn2B'
consumer_secret = 'Ko3QgCOXK2k3GwfrvLaAr0Mk0Z6k2TRGgVAS3qncDNFcdEEkjY'

access_key = '1565715805-E8IdQiws12noARIyEUxeqQeiXnkE64Qs9z9XZ5q'
access_secret = '0jJ2cnlSH59Kcgagj1W8zqaYGB9Uj2RS11uPBWCTz99c0'

# Function to extract tweets


def crawl(username):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        # tweets = api.user_timeline(
        #   screen_name=username, count=200, page=0)
        pages = []  # store indo tweets
        for t in range(10):
            store = api.user_timeline(
                screen_name=username, count=200, page=t, tweet_mode='extended')
            for v in store:
                tweet = v.full_text
                lang = v.lang
                if lang == 'in':  # get only indo tweet
                    if len(tweet) > 1:
                        rtCek = tweet[0]+tweet[1]
                        if rtCek != 'RT':
                            if spam[0] not in tweet and spam[1] not in tweet and spam[2] not in tweet:
                                pages.append(v.full_text)

        # print(len(pages))

        with open(username+".csv", 'w', newline='') as f:
            tulis = csv.writer(f)
            for j in range(len(pages)):
                v = str(pages[j])
                g = str(v.encode('unicode-escape'))  # emoji ubah ke unicode
                tulis.writerow([g])
                if j == 450:  # jumlah row
                    break
    except:
        print('error')

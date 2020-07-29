# remove yg URL, dll.
import tweepy
from textblob import TextBlob
import numpy as np
import csv
import datetime
import nltk
from nltk.tokenize import TweetTokenizer
from collections import defaultdict
import re


def clean2(nama):
    newSentence = []
    userTw = []
    with open(nama+".csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            userTw.append(line)

    for i in range(len(userTw)):
        sent = ''.join(userTw[i].copy())
        token = sent.split()
        newToken = sent.split()
        for x in range(len(token)):
            # tambahkan fitur yg mau dihapus
            if 'http' in token[x]:
                newToken.remove(token[x])
            elif 'ue6f4' in token[x]:
                newToken.remove(token[x])
        concate = ' '.join(newToken).lower()
        newSentence.append(concate)

    with open(nama+".csv", 'w', newline='') as f:
        tulis = csv.writer(f)
        for j in range(len(newSentence)):
            tulis.writerow([newSentence[j]])
    newSentence = []
    userTw = []

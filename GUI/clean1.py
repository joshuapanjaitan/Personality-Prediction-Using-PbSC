# fokus ke replace emoji dan huruf huruf yang tidak jelas
import tweepy
from textblob import TextBlob
import numpy as np
import csv
import datetime
import nltk
from nltk.tokenize import TweetTokenizer
from collections import defaultdict
import re


def checkKey(dict, key):  # fungsi tambahan pengecekan kata jika ada atau tidak
    hasil = ''
    if key in dict:
        hasil = 'yes'
    else:
        hasil = 'No'
    return hasil


kamus = {}


def replace_emoji(key):
    kunci = 'U+'+key
    tes = checkKey(kamus, kunci)
    hasil = ''
    if tes == 'yes':
        hasil = '#'+kamus[kunci]+'#'
    elif tes == 'No':
        hasil = ''
    return hasil


def clean1(nama):
    twToken = TweetTokenizer()
    brendaTw = []
    brendaTwWithEmoji = []
    emoji = []
    with open(nama+".csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            brendaTw.append(line)

    with open("Emoticon_Lib.csv", 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            emoji.append(row)

    for i in range(len(emoji)):
        a = emoji[i][0]
        b = emoji[i][1]
        kamus[a] = b  # masukkan semya emoji ke dic

    # s0 = ''.join(brendaTw[2])
    # twToken.tokenize(s0)

    # pengecekan tweet satu persatu
    for x in range(len(brendaTw)):
        text = ''.join(brendaTw[x])
        text = text[1::]
        text = text.replace("\\n\\", '')
        text = text.replace("'", ' ')
        text = text.replace("...", '')
        text = text.replace("\\", ' ')
        text = text.replace("(", '')
        text = text.replace(")", '')
        text = text.replace("w/", '')
        text = text.replace("U000", 'u')
        sent = text.split()
        xMoji = []
        for t in range(len(sent)):
            u = sent[t]
            if u[0] == 'u':
                if len(u) > 1:
                    if u[1] == '0' or u[1] == '1' or u[1] == '2' or u[1] == '3':
                        u = u.replace('u', '')
                        xMoji.append(u)
        for j in range(len(xMoji)):
            moji = xMoji[j].upper()
            ress = replace_emoji(moji)
            has = 'u'+xMoji[j]
            text = text.replace(has, ress)
            text = re.sub("\s\s+", " ", text)
        brendaTwWithEmoji.append(text)

    # output
    with open(nama+".csv", 'w', newline='') as f:
        tulis = csv.writer(f)
        for j in range(len(brendaTwWithEmoji)):
            tulis.writerow([brendaTwWithEmoji[j]])

    brendaTw = []
    brendaTwWithEmoji = []
    emoji = []

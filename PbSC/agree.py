import dic as dic
import numpy as np
import csv

# khusus mendeteksi HC = high Agreeableness


def getTW(username):  # get tweet
    tweet = []
    with open(username+'.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            tweet.append(line)

    return tweet


def calculateHA(tweet):
    countHA = []
    ratioHA = 0

    for line in dic.highAgreeableness:
        for x in range(len(tweet)):
            text = ''.join(tweet[x])
            if line in text:
                countHA.append(x)

    ress = np.unique(countHA)
    ratioHA = len(ress) / len(tweet)
    hasil = [len(ress),  round(ratioHA, 5)]
    return hasil


def calculateLA(tweet):
    countLA = []
    ratioLA = 0

    for line in dic.lowAgreeableness:
        for x in range(len(tweet)):
            text = ''.join(tweet[x])
            if line in text:
                countLA.append(x)

    ress = np.unique(countLA)
    ratioLA = len(ress) / len(tweet)
    hasil = [len(ress),  round(ratioLA, 5)]
    return hasil


def driver(uname):
    uname = getTW(uname)
    a = calculateHA(uname)
    b = calculateLA(uname)

    hasil = [a[0], a[1], b[0], b[1]]
    return hasil

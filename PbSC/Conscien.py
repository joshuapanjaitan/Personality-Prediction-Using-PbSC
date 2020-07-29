import dic as dic
import numpy as np
import csv

# khusus mendeteksi HC = high Conscientiousnes


def getTW(username):  # get tweet
    tweet = []
    with open(username+".csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            tweet.append(line)

    return tweet


def calculateHC(tweet):
    countHC = []  # hc tweets
    ratioHC = 0  # total tweet - count HC

    for line in dic.highConscientiousnes:
        for x in range(len(tweet)):
            text = ''.join(tweet[x])
            if line in text:
                countHC.append(x)

    ress = np.unique(countHC)
    ratioHC = len(ress) / len(tweet)
    hasil = [len(ress),  round(ratioHC, 5)]
    return hasil


def calculateLC(tweet):
    countLC = []
    ratioLC = 0

    for line in dic.lowConscientiousnes:
        for x in range(len(tweet)):
            text = ''.join(tweet[x])
            if line in text:
                countLC.append(x)

    ress = np.unique(countLC)
    ratioLC = len(ress) / len(tweet)
    hasil = [len(ress),  round(ratioLC, 5)]
    return hasil


def driver(uname):
    uname = getTW(uname)
    a = calculateHC(uname)
    b = calculateLC(uname)

    hasil = [a[0], a[1], b[0], b[1]]
    return hasil

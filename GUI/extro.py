import dic as dic
import numpy as np
import csv

# khusus mendeteksi HC = high Extrovert


def getTW(username):  # get tweet
    tweet = []
    with open(username+".csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            tweet.append(line)

    return tweet


def lenTW(username):
    tweet = []
    with open(username+".csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            tweet.append(line)

    return len(tweet)


def calculateHE(tweet):
    countHE = []
    ratioHE = 0

    for line in dic.highExtrovert:
        for x in range(len(tweet)):
            text = ''.join(tweet[x])
            if line in text:
                countHE.append(x)

    ress = np.unique(countHE)
    ratioHE = len(ress) / len(tweet)
    hasil = [len(ress),  round(ratioHE, 5)]
    return hasil


def calculateLE(tweet):
    countLE = []
    ratioLE = 0

    for line in dic.lowExtrovert:
        for x in range(len(tweet)):
            text = ''.join(tweet[x])
            if line in text:
                countLE.append(x)

    ress = np.unique(countLE)
    ratioLE = len(ress) / len(tweet)
    hasil = [len(ress),  round(ratioLE, 5)]
    return hasil


def driver(uname):
    uname = getTW(uname)
    a = calculateHE(uname)
    b = calculateLE(uname)

    hasil = [a[0], a[1], b[0], b[1]]
    return hasil

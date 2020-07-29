import Conscien as cons
import extro as extro
import agree as agree
import pandas as pd
import numpy as np
import csv
# extrovert hyper parameter
#data = pd.read_csv("username.csv")
data = pd.read_csv("@jooshpn.csv")
pExto = 0.23
qExtro = 0.21

pAgre = 0.22
qAgre = 0.21

pCons = 0.21
qCons = 0.21
uname = ['@jooshpn']
"""
for _ in data['Username']:
    sen = _.replace(" ", "")
    uname.append(sen)
"""

for i in range(len(uname)):
    ressExtro = 'Normal'  # resulf of prediction
    ressAgree = 'Normal'
    ressCons = 'Normal'

    # logic Extroversion
    lenTW = extro.lenTW(uname[i])
    if lenTW != 0:
        extroValue = extro.driver(uname[i])
        if extroValue[1] >= pExto and extroValue[3] <= qExtro:
            ressExtro = 'High'
        elif extroValue[3] >= qExtro and extroValue[1] <= pExto:
            ressExtro = 'Low'

        # logic Agreeableness
        agreValue = agree.driver(uname[i])
        if agreValue[1] >= pAgre and agreValue[3] <= qAgre:
            ressAgree = 'High'
        elif agreValue[3] >= qAgre and agreValue[1] <= pAgre:
            ressAgree = 'Low'

        # logic Conscientiousnes
        conValue = cons.driver(uname[i])
        # print(conValue)
        if conValue[1] >= pCons and conValue[3] <= qCons:
            ressCons = 'High'
        elif conValue[3] >= qCons and conValue[1] <= pCons:
            ressCons = 'Low'
    else:
        ressAgree = 'Normal'
        ressCons = 'Normal'
        ressExtro = 'Normal'
    print(uname[i], ',', ressExtro, ',', ressAgree, ',', ressCons)


# debugging
extroValue = extro.driver(uname[0])
conValue = cons.driver(uname[0])
agreValue = agree.driver(uname[0])
print(extroValue)
print(agreValue)
print(conValue)

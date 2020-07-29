import Conscien as cons
import extro as extro
import agree as agree
import pandas as pd
import numpy as np
import csv
import crawl as crawl
import clean1 as clr1
import clean2 as clr2
import tkinter as tk

pExto = 0.23
qExtro = 0.21

pAgre = 0.22
qAgre = 0.21

pCons = 0.21
qCons = 0.21


def pbsc(username):
    ress = []
    ressExtro = 'Normal'  # resulf of prediction
    ressAgree = 'Normal'
    ressCons = 'Normal'
    crawl.crawl(username)
    clr1.clean1(username)
    clr2.clean2(username)
    # logic Extroversion
    lenTW = extro.lenTW(username)
    if lenTW != 0:
        extroValue = extro.driver(username)
        if extroValue[1] >= pExto and extroValue[3] <= qExtro:
            ressExtro = 'High'
        elif extroValue[3] >= qExtro and extroValue[1] <= pExto:
            ressExtro = 'Low'

        # logic Agreeableness
        agreValue = agree.driver(username)
        if agreValue[1] >= pAgre and agreValue[3] <= qAgre:
            ressAgree = 'High'
        elif agreValue[3] >= qAgre and agreValue[1] <= pAgre:
            ressAgree = 'Low'

        # logic Conscientiousnes
        conValue = cons.driver(username)
        # print(conValue)
        if conValue[1] >= pCons and conValue[3] <= qCons:
            ressCons = 'High'
        elif conValue[3] >= qCons and conValue[1] <= pCons:
            ressCons = 'Low'
    else:
        ressAgree = 'Normal'
        ressCons = 'Normal'
        ressExtro = 'Normal'
    ress.append(username)
    ress.append(ressExtro)
    ress.append(ressAgree)
    ress.append(ressCons)
    return ress

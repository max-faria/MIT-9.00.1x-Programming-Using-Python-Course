# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:44:45 2023

@author: Max
"""

#Criating a Dictonary

beatles = ['She',
 'loves',
 'you',
 'Yeah,',
 'yeah,',
 'yeah',
 'She',
 'loves',
 'you',
 'Yeah,',
 'yeah,',
 'yeah',
 'She',
 'loves',
 'you',
 'Yeah,',
 'yeah,',
 'yeah,',
 'yeah',
 'You',
 'think',
 "you've",
 'lost',
 'your',
 'love',
 'Well,',
 'I',
 'saw',
 'her',
 'yesterday']
def lyrics_to_frequency(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict: # se a palavra já estiver no dicionário aumentar o
        #valor dela em 1
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

mus=lyrics_to_frequency(beatles)

def most_common_words(freqs):
    values = freqs.values()
    #print(values)
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words,best)

def words_often(freqs,minTimes):
    result =[]
    done = False
    while not done:
        temp = most_common_words(freqs)
        print("temp =", temp)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result
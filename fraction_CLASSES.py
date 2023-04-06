# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:22:03 2023

@author: Max
"""

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denommy
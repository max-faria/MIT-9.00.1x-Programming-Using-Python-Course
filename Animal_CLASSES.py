# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:49:15 2023

@author: Max
"""

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def set_name(self, newname):
        self.name = newname
    def set_age(self, newage):
        self.age = newage
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
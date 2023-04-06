# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:38:58 2023

@author: Max
"""
annualInterestRate = 0.2
balance = 3240

monthlyInterestRate = annualInterestRate/12
monthlyPayamentLowerBound = balance/12
monthlyPaymentUpperBound = (balance*(1+monthlyInterestRate**12))/12

guess = (monthlyPayamentLowerBound+monthlyPaymentUpperBound)/2

while abs(balance) > 0:
    for i in range (12):
        balance = balance - guess + ((balance - guess) * monthlyInterestRate)
        if balance > 0 and :
            guess = (guess + monthlyPaymentUpperBound)/2
        elif balance > 0 and:
            guess = (monthlyPayamentLowerBound+guess)/2
        elif balance <= 0:
            break
        print(guess)
    


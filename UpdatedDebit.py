# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:49:16 2023

@author: Max
"""
balance = 4529
annualInterestRate = 0.04

intBalance = balance
monthlyInterestRate = annualInterestRate/12
#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthlyunpaid balance)

monthlyPaymentRate = 0
#upbalance = (balance - lowPayment) + monthlyInterestRate*(balance - lowPayment)

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = intBalance
    elif balance <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)

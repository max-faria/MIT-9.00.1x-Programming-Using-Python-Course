# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:56:44 2023

@author: Max
"""
balance = 42                #outstanding balance on the credit card
annualInterestRate = 0.2    #annual interest rate by decimal
monthlyPaymentRate = 0.04   #minimum monthly payment rate as a decimal
time = 12                   #Time of payment analised

monthlyInterestRate = annualInterestRate/12

#minimumMonthlyPayment = monthlyPaymentRate*previousBalance
#monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
#updatedBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
def remainBalance(balance, time):    
    i = time
    while i > 0:
        if i == 1:
            minimumMonthlyPayment = monthlyPaymentRate*balance
            monthlyUnpaidBalance0 = balance - minimumMonthlyPayment
            updatedBalance = monthlyUnpaidBalance0 + monthlyInterestRate*monthlyUnpaidBalance0
            return round(updatedBalance,2)                      
        else:
            minimumMonthlyPayment = monthlyPaymentRate*remainBalance(balance, time-1)
            monthlyUnpaidBalance = remainBalance(balance, time-1) - minimumMonthlyPayment
            updatedBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
            i -= 1
            return round(updatedBalance,2)

print(remainBalance(42, 12))

            


# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 06:55:04 2023

@author: Max
"""

import pylab as plt

mySamples =[]
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range (0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

## first trial, all plots in one figure
plt.plot(mySamples, myLinear)     #all plot in one figure
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

#second trial, one plot for figure
plt.figure('Lin')
plt.clf() #to clean the figure to avoid overplotting
plt.ylim(0,1000)
plt.title('Linear Function')
plt.xlabel('Samples Points')    
plt.ylabel('Linear Function')
plt.plot(mySamples, myLinear, 'r')

plt.figure('Quad')
plt.clf()
plt.ylim(0,1000)
plt.title('Quadratic Plot')
plt.xlabel('Simples Points')
plt.ylabel('Quadratic Funtion')
plt.plot(mySamples, myQuadratic, 'g')

plt.figure('Cubic')
plt.clf()
plt.plot(mySamples, myCubic, '-')

plt.figure('Exponential')
plt.clf()
plt.plot(mySamples, myExponential, '')

## Ploting two functions in one figure
plt.figure('Lin Qua')
plt.clf()
plt.title('Linear vs Quadratic')
plt.plot(mySamples, myLinear, 'b-', label = 'Linear', linewidth=2.0)
plt.plot(mySamples, myQuadratic, 'ro', label = 'Quadratic', linewidth=1.5)
plt.legend(loc = 'upper left') # the loc of legend position must come after the plot command

plt.figure('Cub Exp')
plt.clf()
plt.title('Cubic vs Exponential')
plt.plot(mySamples, myCubic, 'g^', label = 'Cubic', linewidth=2.5)
plt.plot(mySamples, myExponential, 'r--', label = 'Exponential', linewidth=3.0)
plt.legend()

## Using subplots
## subplot takes three arguments: (XYZ)
## X -> number of lines
## Y -> number of collums
## Z -> position

plt.figure('Lin Qua')
plt.clf()
plt.subplot(211)
plt.title('Linear vs Quadratic')
plt.ylim(0,900)
plt.ylabel('Function Values')
plt.plot(mySamples, myLinear, 'b-', label = 'Linear', linewidth=2.0)
plt.legend('upper left') # it's necessary to give the commando for show the legend
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples, myQuadratic, 'ro', label = 'Quadratic', linewidth=1.5)
plt.legend(loc = 'upper left') # the loc of legend position must come after the plot command
plt.xlabel('Simple Points')
plt.ylabel("Function Values")


plt.figure('Cub Exp')
plt.clf()
plt.subplot(121)
plt.title('Cubic vs Exponential')
plt.ylim(0,14000)
plt.ylabel('Function Values')
plt.xlabel('Simples Points')
plt.plot(mySamples, myCubic, 'g^', label = 'Cubic', linewidth=2.5)
plt.legend()
plt.subplot(122)
plt.ylim(0,14000)
plt.xlabel('Simple Points')
plt.plot(mySamples, myExponential, 'r--', label = 'Exponential', linewidth=3.0)
plt.legend()

## Changing Scales

plt.figure('Cub Exp')
plt.clf()
plt.title('Cubic vs Exponential')
plt.xlabel('Simples Points')
plt.ylabel('Function Values')
plt.yscale('log')
plt.plot(mySamples, myCubic, 'g^', label = 'Cubic', linewidth=2.5)
plt.plot(mySamples, myExponential, 'r--', label = 'Exponential', linewidth=3.0)
plt.legend()

## RETIREMENT PLAN
def retire (monthly, rate, terms):
    """
    Parameters
    ----------
    monthly : int monthly invested value.
    rate : float interest tax.
    terms : number of months.

    Returns
    -------
    base : x values.
    savings : y values, savings of the month.

    """
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1+mRate) + monthly]
    return base, savings

def displayRetireMonthlies(monthlies, rate, terms):
    """
    
    Parameters
    ----------
    monthlies : monthly amount.
    rate : interest rate.
    terms :number of months.

    Returns
    -------
    a plot

    """
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals,yvals, label='retire:' + str(monthly))
        plt.legend(loc='upper left')

displayRetireMonthlies([500,600,700,800,900,1000], 0.5, 10*12)

def displayRetireRates(month, rates, terms):
    """

    Parameters
    ----------
    month : int monthly amount.
    rates : float interest rate.
    terms : period of time.


    """
    plt.figure()
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals,yvals, label = 'retire: ' + str(month) + str(int(rate*100)))
        plt.legend(loc='upper left')
         


displayRetireRates(800, [.03, .05, .07], 40*12)    
        
def displayRetirementWithMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--', '^']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel+rateLabel,
                    label = 'retire:'+str(monthly)+ ':' + str(int(rate*100)))
            plt.legend(loc = 'upper left')

# displayRetireWMonthsAndRates([500,700,900,1100], [0.03, 0.05, 0.07], 40*12)    

 
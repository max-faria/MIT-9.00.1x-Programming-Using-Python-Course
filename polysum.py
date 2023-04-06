# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:32:29 2023

@author: Max
"""

import math

def polysum (n,s):
    """

    Parameters
    ----------
    n : number os sides of a regular polygon.
    s : length of each side.

    Returns
    -------
    sum of the area with the square of the perimeter.

    """
    area = (0.25*n*s**2)/math.tan(math.pi/n) #Calculate the area
    perimeter = n*s                          #Calculate the perimeter 
    return round(area + perimeter**2, 4)
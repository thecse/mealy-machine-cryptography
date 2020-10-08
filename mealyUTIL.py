# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:32:51 2020

@author: Rohan
"""

def mealy(i, state):                                     
    if state==0:                                         
        if i==0:                                         
            return 2, 0
        else:
            return 5, 1
    elif state==1:
        if i==0:
            return 2, 2
        else:
            return 3, 3
    elif state==2:
        if i==0:
            return 4, 4
        else:
            return 5, 5
    elif state==3:
        if i==0:
            return 3, 0
        else:
            return 1, 1
    elif state==4:
        if i==0:
            return 2, 2
        else:
            return 3, 3
    elif state==5:
        if i==0:
            return 4, 4
        else:
            return 5, 5

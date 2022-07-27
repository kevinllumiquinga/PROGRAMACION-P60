# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:46:46 2022

@author: Kevin Llumiquinga.
"""

import math 
def fibo(n):
    n=n+1
    p1=(1+math.sqrt(5))**n
    p2=(1-math.sqrt(5))**n
    d1=2**n
    d2=math.sqrt(5)
    fn=(p1-p2)/(d1*d2)
    print(fn)
fibo(8)
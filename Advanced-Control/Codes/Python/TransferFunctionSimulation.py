#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 23:44:06 2018

@author: eddardd
"""

import numpy as np
import pandas as pd
import seaborn as sns
import control as ctrl
import matplotlib.pyplot as plt

from scipy.constants import g

def define_model(M, m, l, dmf, fc):
    """
        Given the parameters, this fuction returns
        transfer functions for variables x and theta,
        and state-space model for the whole system,
        for the inverted pendulum.
        Parameter description:
            - M: cart mass
            - m: pendulum mass
            - l: pole length
            - dmf: joint friction
            - fc: cart friction
    """
    ## State space
    A = np.array([[0, 1, 0, 0],
                  [0, -fc/M, m*g/M, dmf/(M*l)],
                  [0,0,0,1],
                  [0, -fc/(M*l), (M+m)*g/(M*l), 
                   (M+m)*dmf/(M*m*(l**2))]])
    B = np.array([[0],
                  [1/M],
                  [0],
                  [1/(M*l)]])
    C = np.array([[1,0,0,0],
                  [0,0,1,0]])
    D = np.array([[0],
                  [0]])
    
    ss_model = ctrl.ss(A, B, C, D)
    ## Transfer Functions
    s = ctrl.tf([1,0],[1]) # Frequency variable
    
    Tx = (m*(l**2)*(s**2) - dmf*s - m*g*l)/ \
    (M*m*(l**2)*(s**4) - ((M+m)*dmf - m*(l**2)*fc)*(s**3) - \
    (dmf * fc + (M+m)*m*g*l)*(s**2) - m*g*l*fc*s)
    
    Tt = (m*l*s**2)/(M*m*(l**2)*(s**3)\
           - ((M+m)*dmf - m*(l**2)*fc)*(s**2) - \
          (dmf * fc + (M+m)*m*g*l)*s - m*g*l*fc)

    return (Tx, Tt, ss_model)

"""
    Problem variables
"""
M = 4.8        # Cart mass
m = 0.356      # Pendulum mass
l = 0.56       # Pole length
dmf = 0.035    # Joint friction
fc = 4.9       # Cart friction


"""
    Transfer functions
"""
s = ctrl.tf([1,0],[1]) # Frequency variable
Tx, Tt, SS = define_model(M, m, l, dmf, fc)

"""
    Root Locus
"""



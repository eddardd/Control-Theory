#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 02:09:11 2018

@author: eddardd
"""

import numpy as np
import matplotlib.pyplot as plt

def y_impulse(t,a):
    """
        System's impulse response
    """
    return np.exp(-2*t)*(a*np.cos(2*np.sqrt(2)*t) + 
                  ((6-4*a)/(4*np.sqrt(2)))*np.cos(2*np.sqrt(2)*t))

def y_step(t,a):
    return .25 + .25*np.exp(-2*t)*(np.sqrt(2)*np.cos(2*np.sqrt(2)*t) +
                                  (2*a-1)*np.sin(2*np.sqrt(2)*t))

a_vec = [-4, -1, 0, 1, 4]
t = np.linspace(0,3,300)

plt.figure()
for a in a_vec:
    plt.plot(t,y_impulse(t,a), label = 'a = {}'.format(a))
plt.grid()
plt.title(r'System impulse response for values of $\alpha$')
plt.legend()

plt.figure()
for a in a_vec:
    plt.plot(t,y_step(t,a), label = r'$\alpha$ = {}'.format(a))
plt.grid()
plt.title(r'System step response for values of $\alpha$')
plt.legend()
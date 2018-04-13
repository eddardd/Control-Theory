#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 01:55:21 2018

@author: eddardd
"""

import numpy as np
import matplotlib.pyplot as plt

def x1(t):
    """
        First system's state variable
    """
    return (1/12)*t*np.exp(-t) - (1/36)*np.exp(-t) + (1/36)*np.exp(-4*t)

def x2(t):
    """
        Second system's state variable
    """
    return -(1/12)*t*np.exp(-t) + (1/9)*np.exp(-t) - (1/9)*np.exp(-4*t)

def y(t):
    """
        The system's output
    """
    return (1/3)*t*np.exp(-t) + (23/36)*np.exp(-t) - (23/36)*np.exp(-4*t)

def u(t):
    """
        System's input
    """
    return np.exp(-t)

t = np.linspace(0,10,400)

fig, ax = plt.subplots(1,2,figsize=(12,6))

ax[0].plot(t,x1(t),label = r'$x_1$')
ax[0].plot(t,x2(t),label = r'$x_2$')
ax[0].grid()
ax[0].set_title('State variables response')
ax[0].legend()

ax[1].plot(t,y(t),label = 'y')
ax[1].plot(t,u(t),label = 'u')
ax[1].grid()
ax[1].set_title('Input and Output response')
ax[1].legend()





























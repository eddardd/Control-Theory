#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 19:39:38 2018

@author: eddardd

-- Exercise 1 plots
"""

import numpy as np
import matplotlib.pyplot as plt

"""
    Responses
"""

T = np.linspace(0,3,300)
free_response = np.exp(-2*T)*(2*np.cos(T) + 5*np.sin(T))
impulse_response = np.exp(-2*T)*(3*np.cos(T) + 8*np.sin(T))
step_response = 1 + np.exp(-2*T)*(np.cos(T)+4*np.sin(T))

"""
    Plots
"""

plt.figure()
plt.plot(T,free_response, label = 'Free response')
plt.plot(T,impulse_response, label = 'Impulse response')
plt.plot(T,step_response, label = 'Step response')
plt.grid()
plt.legend()
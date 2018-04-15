#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 21:05:49 2018

@author: eddardd
"""

import numpy as np
import control as ctrl
import equations as eq
import matplotlib.pyplot as plt


t0 = 0; tf = 50; n = 10000;
amplitudes  = [10, 25, 50]
frequencies = [1, 25, 30]
responses = []
lin_responses = []
sys_pi = eq.linear_equations(sp = 1)

for i in range(3):
    for j in range(3):
        T, x = eq.ODEeuler(eq.nonlinear_equations, 
                           np.array([[0,0,0,0]]),
                           amplitudes[i],frequencies[j],
                           n = n, tf = tf, method = 'Midpoint',
                           inp = 'Sinusoid')
        _, x_pi, _ = ctrl.forced_response(sys_pi, T = T, 
                                          U = amplitudes[i]*np.sin(frequencies[j]*T),
                                          X0 = np.array([0,0,np.pi,0]))
        responses.append(x)
        lin_responses.append(x_pi)



(fig, ax) = plt.subplots(3,3,figsize=(14,14), 
                         sharex = False,sharey = False)
plt.suptitle('Pendulum\'s angle response')
for i in range(3):
    for j in range(3):
        k = 3*i+j
        ax[i,j].plot(T, responses[k][:,0], label = 'Nonlinear response')
        ax[i,j].plot(T, np.pi-lin_responses[k][0,:], label = 'Linear response')
        ax[i,j].set_title(r'A = {}, $\omega$ = {}'.format(amplitudes[i],frequencies[j]))
        ax[i,j].grid()
        ax[i,j].legend()

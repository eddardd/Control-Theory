#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:52:25 2018

@author: eddardd
"""

import numpy as np
import control as ctrl
import equations as eq
import matplotlib.pyplot as plt


t0 = 0; tf = 50; n = 10000;

T, x_nonlin = eq.ODEeuler(eq.nonlinear_equations, 
                          np.array([[0,0,0,0]]),
                          n = n, tf = tf, method = 'Midpoint',
                          inp = 'Step')

sys_0  = eq.linear_equations(sp = 0)
sys_pi = eq.linear_equations(sp = 1)

_, x_pi = ctrl.step_response(sys_pi, T = T,
                             X0 = np.array([0,0,np.pi,0]))


fig, ax  = plt.subplots(1,2,figsize=(12,6))
plt.suptitle('Linear vs. Nonlinear Step response in the upward position')

ax[0].plot(T, x_nonlin[:,0], 'k-', label = 'Nonlinear')
ax[0].plot(T, x_pi[0,:], 'b--', label = 'Linear')
ax[0].legend()
ax[0].grid()
ax[0].set_ylabel(r'Cart position $x$ [meters]')
ax[0].set_xlabel('Time [seconds]')

ax[1].plot(T, x_nonlin[:,2], 'k-', label = 'Nonlinear')
ax[1].plot(T, np.pi-x_pi[2,:], 'b--', label = 'Linear')
ax[1].legend()
ax[1].grid()
ax[1].set_ylabel(r'Angle $\theta$ [radians]')
ax[1].set_xlabel('Time [seconds]')

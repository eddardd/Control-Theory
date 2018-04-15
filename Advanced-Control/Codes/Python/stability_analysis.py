#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 18:48:36 2018

@author: eddardd

Stabilization in upward position
"""

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
from equations import *

sys_unstable = linear_equations(sp = 0)
(A, B, C, D) = ctrl.ssdata(sys_unstable)
K = ctrl.place(A, B, [-3.5, -3.6, -3.7, -3.8])
A_stable = A - np.dot(B,K)
sys_stable = ctrl.ss(A_stable, B, np.eye(4), np.zeros((4,1)))

t0 = 0; tf = 50; n = 5000;
x_stable, T = ctrl.step(sys_stable,np.linspace(t0,tf,n))

fig, ax = plt.subplots(2,2, figsize = (12,12))

plt.suptitle('Stable linearized step response summary')

ax[0,0].set_title('Cart position')
ax[0,0].plot(np.linspace(t0,tf,len(x_stable[:,0])),x_stable[:,0],'k-')
ax[0,0].set_ylabel('Cart position [meters]')
ax[0,0].set_xlabel('Time [seconds]')
ax[0,0].grid()

ax[0,1].set_title('Pendulum angle')
ax[0,1].plot(np.linspace(t0,tf,len(x_stable[:,2])),x_stable[:,2],'k-')
ax[0,1].set_ylabel('Pendulum angle [Radians]')
ax[0,1].set_xlabel('Time [seconds]')
ax[0,1].grid()

ax[1,0].set_title('Position phase portrait')
ax[1,0].plot(x_stable[:,0], x_stable[:,1], 'k')
ax[1,0].plot(x_stable[0,0], x_stable[0,1], 'r+')
ax[1,0].plot(x_stable[-1,0], x_stable[-1,1], 'r+')
ax[1,0].set_ylabel('Cart velocity [meters/sec]')
ax[1,0].set_xlabel('Cart position [meters]')
ax[1,0].grid()

ax[1,1].set_title('Angle phase portrait')
ax[1,1].plot(x_stable[:,2], x_stable[:,3], 'k')
ax[1,1].plot(x_stable[0,2], x_stable[0,3], 'r+')
ax[1,1].plot(x_stable[-1,2], x_stable[-1,3], 'r+')
ax[1,1].set_ylabel('Angular velocity [radians/sec]')
ax[1,1].set_xlabel('Pendulum angle [radians]')
ax[1,1].grid()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:53:04 2018

@author: eddardd
"""

import numpy as np
import matplotlib.pyplot as plt
from equations import *

t0 = 0; tf = 50; n = 1000; y0 = [0, 0, 0, 0]
T, x = ODEeuler(nonlinear_equations, np.array([[0,0,0,0]]),
                tf = 50, method = 'Midpoint', inp = 'Step')

fig, ax = plt.subplots(2,2,figsize=(12,12))

plt.suptitle('Step response summary')

ax[0,0].set_title('Cart position')
ax[0,0].plot(np.linspace(t0,tf,len(x[:,0])),x[:,0],'k-')
ax[0,0].set_ylabel('Cart position [meters]')
ax[0,0].set_xlabel('Time [seconds]')
ax[0,0].grid()

ax[0,1].set_title('Pendulum angle')
ax[0,1].plot(np.linspace(t0,tf,len(x[:,2])),x[:,2],'k-')
ax[0,1].set_ylabel('Pendulum angle [Radians]')
ax[0,1].set_xlabel('Time [seconds]')
ax[0,1].grid()

ax[1,0].set_title('Position phase portrait')
ax[1,0].plot(x[:,0], x[:,1], 'k')
ax[1,0].plot(x[0,0], x[0,1], 'r+')
ax[1,0].plot(x[-1,0], x[-1,1], 'r+')
ax[1,0].set_ylabel('Cart velocity [meters/sec]')
ax[1,0].set_xlabel('Cart position [meters]')
ax[1,0].grid()

ax[1,1].set_title('Angle phase portrait')
ax[1,1].plot(x[:,2], x[:,3], 'k')
ax[1,1].plot(x[0,2], x[0,3], 'r+')
ax[1,1].plot(x[-1,2], x[-1,3], 'r+')
ax[1,1].set_ylabel('Angular velocity [radians/sec]')
ax[1,1].set_xlabel('Pendulum angle [radians]')
ax[1,1].grid()
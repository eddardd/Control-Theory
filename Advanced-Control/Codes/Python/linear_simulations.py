#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:52:25 2018

@author: eddardd
"""

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
from equations import *

t0 = 0; tf = 50; n = 5000;

sys_unstable = linear_equations(sp = 1)
sys_stable = linear_equations(sp = 1)

x_unstable, T = ctrl.step(sys_unstable,np.linspace(t0,tf,n), X0 = [0, 0, 0, 0])
x_stable, T = ctrl.step(sys_stable,np.linspace(t0,tf,n))

fig, ax = plt.subplots(2,2, figsize = (12,12))

plt.suptitle('Stable linearized step response summary')

ax[0,0].set_title('Cart position')
ax[0,0].plot(np.linspace(t0,tf,len(x_unstable[:,0])),x_unstable[:,0],'k-')
ax[0,0].set_ylabel('Cart position [meters]')
ax[0,0].set_xlabel('Time [seconds]')
ax[0,0].grid()

ax[0,1].set_title('Pendulum angle')
ax[0,1].plot(np.linspace(t0,tf,len(x_unstable[:,2])),x_unstable[:,2],'k-')
ax[0,1].set_ylabel('Pendulum angle [Radians]')
ax[0,1].set_xlabel('Time [seconds]')
ax[0,1].grid()

ax[1,0].set_title('Position phase portrait')
ax[1,0].plot(x_unstable[:,0], x_unstable[:,1], 'k')
ax[1,0].plot(x_unstable[0,0], x_unstable[0,1], 'r+')
ax[1,0].plot(x_unstable[-1,0], x_unstable[-1,1], 'r+')
ax[1,0].set_ylabel('Cart velocity [meters/sec]')
ax[1,0].set_xlabel('Cart position [meters]')
ax[1,0].grid()

ax[1,1].set_title('Angle phase portrait')
ax[1,1].plot(x_unstable[:,2], x_unstable[:,3], 'k')
ax[1,1].plot(x_unstable[0,2], x_unstable[0,3], 'r+')
ax[1,1].plot(x_unstable[-1,2], x_unstable[-1,3], 'r+')
ax[1,1].set_ylabel('Angular velocity [radians/sec]')
ax[1,1].set_xlabel('Pendulum angle [radians]')
ax[1,1].grid()
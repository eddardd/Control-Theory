#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 22:53:44 2018

@author: eddardd
"""
import imageio
import numpy as np
import matplotlib.pyplot as plt
from equations import *

## Contants
M   = 4.800     # Cart mass
m   = 0.356     # Pendulum mass
L   = 0.560     # Pole length

## Simulation
t0 = 0; tf = 50; n = 5000
T, x = ODEeuler(nonlinear_equations, np.array([[0,0,0,0.1]]),
                n = n, tf = tf, method = 'Midpoint', inp = 'Free')

## Frames
for i in range(0,n,10):
    drawCartPend(x[i,:], m, M, 2, i)
    plt.close('all')
    
file_names = ['animation/frame{}.png'.format(i) for i in range(0,n,10)]
images = []
for filename in file_names:
    images.append(imageio.imread(filename))
imageio.mimsave('animation/CartPend.gif', images)


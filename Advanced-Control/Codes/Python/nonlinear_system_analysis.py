#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:04:08 2018

@author: eddardd
"""

import numpy as np

def CartPend(x, M = 4.8, m = 0.356, l = 0.56,
             g = 9.806, bx = 4.9, bth = 0.035,
             F = 0):
    """
        This function creates the two
        ODEs for the cart-pendulum system
        with parameters:
            - x: state vector
            - M: cart mass
            - m: pendulum mass
            - l: pole length
            - g: gravity acceleration
            - bx: track friction
            - bth: joint friction
            - F: applied force
    """
    Delta = M + m*(1-np.cos(x[2])**2)
    Cx = np.cos(x[2]); Sx = np.sin(x[2])
    #bx = fc*np.sign(x[1])
    
    dx = np.zeros((4,))
    dx[0] = x[1]
    dx[1] = (F - bx*x[1] - m*l*Sx*x[3]**2 /
             m*g*Cx*Sx + bth*Cx*x[3])/Delta
    dx[2] = x[3]
    
    dx[3] = (Cx*F - Cx*bth*x[1] + \
             (M+m)*bth*x[3]/(m*l**2) + \
             (M+m)*g*Sx - \
             m*l*Sx*Cx*(x[3]**2)) /(Delta*l)
    return dx

def system_ODEsolver(f, xo, to = 0, tf = 10, 
                     step = 0.01, inp = 'Free',
                     method = 'Euler'):
    
    """
        Euler methods for solving non-linear
        systems of ODEs
    """
    
    n = int((tf - to)/step)
    _, p = xo.shape
    
    T = np.zeros((n,));  T[0] = to
    x = np.zeros((n,p)); x[0,:] = xo
    t = np.linspace(to, tf, n)
    
    if inp == 'Free':
        F = np.zeros((n,))
    elif inp == 'Impulse':
        F = np.zeros((n,))
        F[0] = 1
    elif inp == 'Step':
        F = np.ones((n,))
    elif inp == 'Sinusoid':
        F = np.sin(t)
    
    for i in range(n-1):
        if method == 'Euler':
            T[i+1] = T[i] + step
            x[i+1,:] = x[i,:] + f(x[i,:], F = F[i]) * step
        if method == 'Heun':
            T[i+1] = T[i] + step
            tmp    = x[i,:] + f(x[i,:], F = F[i]) * step
            x[i+1,:] = x[i] + (f(x[i,:], F = F[i]) + f(tmp, F = F[i])) * (step / 2)
        elif method == 'Midpoint':
            #Tm     = T[i] + .5 * step
            T[i+1] = T[i] + step
            xm     = x[i,:] + f(x[i,:], F = F[i]) * (step / 2)
            x[i+1,:] = x[i,:] + f(xm, F = F[i]) * step
    return (T,x)
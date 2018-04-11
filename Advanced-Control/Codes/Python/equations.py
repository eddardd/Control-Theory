#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:43:49 2018

@author: eddardd
"""

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
from numpy import cos, sin

def nonlinear_equations(x,F):
    """
        This function implements the vector
        field that characterizes the non-
        linear equations of inverted pendulum
    """
    ## Constants
    M   = 4.800     # Cart mass
    m   = 0.356     # Pendulum mass
    L   = 0.560     # Pole length
    bth = 0.035     # Joint Friction
    bx  = 4.900     # Cart Friction
    I   = 0.006     # Pole inertia moment
    g = 9.806       # Gravitational acceleration
    
    ## Equations
    
    alpha = (M+m)*(m*(L**2)+I) - (m*L*cos(x[2]))**2
    #F = 1 # Step response
    
    dx = np.zeros((4,))
    
    
    dx[0] = x[1]
    dx[2] = x[3]
    dx[1] = ((m * L**2 + I)*(F + m*L*x[3]*sin(x[2]) - bx*x[1]) + m*L*cos(x[2])*(m*g*L*sin(x[2]) - bth*x[3]))/alpha
    dx[3] = ((M+m)*(m*g*L*sin(x[2]) - bth*x[3]) + m*L*cos(x[2])*(F + m*L*sin(x[2])*x[3]-bx*x[1]))/alpha
    
    return dx

def linear_equations(sp = 0):
    """
        This function constructs a linear model
        for the inverted pendulum system.
    """
    ## Constants
    M   = 4.800     # Cart mass
    m   = 0.356     # Pendulum mass
    L   = 0.560     # Pole length
    bth = 0.035     # Joint Friction
    bx  = 4.900     # Cart Friction
    I   = 0.006     # Pole inertia moment
    g = 9.806       # Gravitational acceleration
    
    if sp != 0 and sp != 1:
        print('Error: bad input arguments')
        exit()
    
    alpha = (M+m)*(I + m*L**2) - (m*L)**2
    
    if sp == 0:
        A = np.array([[0,                     1,                  0,                0],
                      [0, - (I+m*L**2)*bx/alpha, ((m*L)**2)*g/alpha,   -m*L*bth/alpha],
                      [0,                     0,                  0,                1],
                      [0,       -(m*L*bx)/alpha,  (M+m)*m*g*L/alpha, -(M+m)*bth/alpha]])
    
        B = np.array([[0],
                      [(m*L**2 + I)/alpha],
                      [0],
                      [m*L/alpha]])
    if sp == 1:
        A = np.array([[0,                     1,                  0,                0],
                      [0, - (I+m*L**2)*bx/alpha,-((m*L)**2)*g/alpha,    m*L*bth/alpha],
                      [0,                     0,                  0,                1],
                      [0,        (m*L*bx)/alpha, -(M+m)*m*g*L/alpha, -(M+m)*bth/alpha]])
    
        B = np.array([[0],
                      [(m*L**2 + I)/alpha],
                      [0],
                      [-m*L/alpha]])
    C = np.eye(4); D = np.zeros((4,1))
    return ctrl.ss(A, B, C, D)
def ODEeuler(f, xo, to = 0, tf = 10, 
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
    elif inp == 'Ramp':
        F = T
    elif inp == 'Sinusoid':
        F = 1*np.sin(5*t)
    
    for i in range(n-1):
        if method == 'Euler':
            T[i+1] = T[i] + step
            x[i+1,:] = x[i,:] + f(x[i,:],F[i]) * step
        if method == 'Heun':
            T[i+1] = T[i] + step
            tmp    = x[i,:] + f(x[i,:], F[i]) * step
            x[i+1,:] = x[i] + (f(x[i,:],F[i]) + f(tmp, T[i+1])) * (step / 2)
        elif method == 'Midpoint':
            #Tm     = T[i] + .5 * step
            T[i+1] = T[i] + step
            xm     = x[i,:] + f(x[i,:], F[i]) * (step / 2)
            x[i+1,:] = x[i,:] + f(xm, F[i]) * step
        """
        if x[i+1,0] > 1 :
            x[i+1,0] = 1
        if x[i+1,0] < -1:
            x[i+1,0] = -1
        if x[i+1,2] > np.pi/2:
            x[i+1,2] = np.pi/2
        if x[i+1,2] < -np.pi/2:
            x[i+1,2] = -np.pi/2 
        """
    return (T,x)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 22:09:36 2018

@author: eddardd
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def drawCartPend(x, m, M, L):
    """
        This function is responsable to
        generate figures with the dynamic
        behavior of the Cart pend. It re-
        ceives as arguments,
            - x: the present state of the
            system,
            - m: the pendulum's mass
            - M: the cart's mass
            - L: the pole's length
    """
    # Relevant state
    position = x[0]
    angle = x[2]
    
    # Dimensions
    W  = np.sqrt(M/5)     # Cart width
    H  = 0.5*np.sqrt(M/5) # Cart heigth
    mr = 0.4*np.sqrt(m/5) # pendulum radius
    
    # Position
    y   = H/2             # Cart's vertical position
    
    px = position + L*np.sin(angle)
    py = position + L*np.cos(angle)
    
    # Cart drawing
    figure = plt.figure(figsize=(16,8))
    ax = figure.add_subplot(111, aspect = 'equal')
    ax.set_xlim(-4,4); ax.set_ylim(-3,5)
    ax.axhline(color = 'k')
    #ax.plot([-10,10],[0,0],'k-')
    
    ax.add_patch(patches.Rectangle((position-W/2,y-H/2), W, H,
                                   color = 'r',fill = True))
    ax.plot([position, px],[y, py], 'k-')
    ax.add_patch(patches.Circle((px,py),radius = mr, color = 'k'))
    
    
    
    
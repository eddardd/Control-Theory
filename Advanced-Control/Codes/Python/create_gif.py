#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:12:56 2018

@author: eddardd
"""

import imageio

file_names = ['animation/frame{}.png'.format(i) for i in range(0,1000,5)]
images = []
for filename in file_names:
    images.append(imageio.imread(filename))
imageio.mimsave('animation/CartPend.gif', images)

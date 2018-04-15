#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 18:49:21 2018

@author: eddardd
"""

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
from equations import *


sys_unstable = linear_equations(sp = 0)

tf_unst = ctrl.ss2tf(sys_unstable)
nums, dens = ctrl.tfdata(sys_unstable)

Tx     = ctrl.tf(nums[0][0], dens[0][0])
Ttheta = ctrl.tf(nums[2][0], dens[2][0])

print(ctrl.bode(Ttheta))




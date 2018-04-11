#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:39:20 2018

@author: eddardd
"""

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
from equations import *

sys_stable = linear_equations(sp = 1)
sys_unstable = linear_equations(sp = 0)

(A_unstable, _, _, _) = ctrl.ssdata(sys_unstable)
(A_stable, _, _, _) = ctrl.ssdata(sys_stable)

poles_unstable, _ = np.linalg.eig(A_unstable)
poles_stable, _ = np.linalg.eig(A_stable)
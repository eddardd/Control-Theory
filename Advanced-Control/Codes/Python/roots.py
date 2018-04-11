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

fig, ax = plt.subplots(1,2,figsize=(14,6),sharey=True)
plt.suptitle('Eigenvalues of linearized system')

ax[0].set_title(r'$\theta_{sp} = 0$')
ax[0].plot(poles_unstable, [0,0,0,0], 'rx')
ax[0].set_xlabel('Real')
ax[0].set_ylabel('Imaginary')
ax[0].grid()
ax[0].axvline()

ax[1].set_title(r'$\theta_{sp} = \pi$')
ax[1].plot(np.real(poles_stable), np.imag(poles_stable), 'rx')
ax[1].set_xlabel('Real')
ax[1].set_ylabel('Imaginary')
ax[1].grid()
ax[1].axvline()
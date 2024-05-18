#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:32:34 2024

@author: andrew_s
"""

import matplotlib.pyplot as plt
import numpy as np

bf = np.array([10,10])
bfs = 8
bfh = 30

arc = np.arange(0+bfh,180+bfh,1)

rng = 60

xs = rng*np.cos(np.radians(arc))+bf[0]+rng*np.cos(np.radians(bfh))/3

ys = rng*np.sin(np.radians(arc))+bf[1]+rng*np.sin(np.radians(bfh))/3

lar = np.sqrt(xs**2+ys**2)

fig, axs = plt.subplots(1,2)

axs[0].plot(xs,ys,'-')
axs[0].plot(bf[0]+rng*np.cos(np.radians(bfh))/3,bf[1]+rng*np.sin(np.radians(bfh))/3,'r.')
axs[0].plot(bf[0],bf[1],'bo')
axs[0].set_aspect('equal')
axs[0].set_xlim(-75,100)
axs[0].grid()
axs[1].plot(180-arc+bfh,lar,'-')
axs[1].grid()
#fig.tight_layout()

plt.show()

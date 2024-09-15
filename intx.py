# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:18:57 2024

@author: shobeas1
"""
import numpy as np
import matplotlib.pyplot as plt

def move(in_pos,in_spd,in_hdg):
    [x,y,h] = np.add(in_pos,in_spd*np.array([np.cos(np.radians(in_hdg)), np.sin(np.radians(in_hdg)),0]))
    return [x,y,h]
    
intx = 'cata'
arc = np.arange(-60,60,1)
bf = np.array([0,0])
rf = np.array([10,5])
bfs = 0.8
rfs = 0.8

bfh = 0
rfh = 180

hca = np.abs(bfh - rfh)

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,layout='constrained')

while bf[0] < rf[0]:
    pos = np.subtract(rf, bf)
    rng = np.linalg.norm(pos)
    brg = np.degrees(np.arctan(pos[1]/pos[0]))
    el = np.degrees(np.arctan(pos[2]/pos[0]))
    ata = bfh - brg
    aa = rfh - brg
    ax3.plot(bf[0],aa,'bo')
    ax4.plot(bf[0],rng,'b^')
    cc = 180 - rfh + brg
    ax1.plot(ata, el, 'gs')
    # ax2.plot(rf[0],rf[1],'r<')
    # ax2.plot(bf[0],bf[1],'b>')
    ax2.quiver(rf[0],rf[1],rfs*np.cos(np.radians(rfh)),rfs*np.sin(np.radians(rfh)),color='r',pivot='tip')
    ax2.quiver(bf[0],bf[1],bfs*np.cos(np.radians(bfh)),bfs*np.sin(np.radians(bfh)),color='b',pivot='tip')
    if intx == 'pure':
        bfh += -ata
    elif intx == 'hot':
        bfh = brg + 1.5*cc
    else:
        bfh = brg + cc
    bf = move(bf,bfs,bfh)
    rf = move(rf,rfs,rfh)

ax1.set_xlim(-60,60)
ax1.set_ylim(0,15)
ax1.set_box_aspect(1)
ax1.grid()

ax2.set_xlim(-5,12)
ax2.set_ylim(-5,8)
ax2.set_aspect('equal')
ax2.grid()

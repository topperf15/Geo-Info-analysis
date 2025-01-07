#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 08:12:43 2024

@author: andrew_s
"""

import numpy as np

def merc_proj(R,lamda,phi):
    X = R * (lamda);
    Y = R * np.log(np.tan(np.pi/4 + phi/2));
    return X,Y

lamda = np.linspace(-np.pi,np.pi,19);
phi = np.linspace(-4*np.pi/9,4*np.pi/9,9);    
R = 1;

[X,Y] = merc_proj(R,lamda,phi);

xm, ym = np.meshgrid(X,Y)

import matplotlib.pyplot as plt

for i in range(19):
    plt.plot(xm[:,i],Y,color='k')
for j in range(9):
    plt.plot(X,ym[j,:],color='k')
plt.plot(xm,ym,marker='.', color='c', linestyle='none')
plt.grid()
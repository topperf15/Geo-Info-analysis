#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:29:12 2025

@author: andrew_s
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./Airports_subset.csv')

y = df["runway_length_ft"].tolist()
x = df["NM"].tolist()

x_multi = [df[df['runway_length_ft']>n]["NM"].tolist()for n in [8000, 6000, 3000]]
n_bins = 10
x_bins = np.arange(350,1150,100)

fig, ax = plt.subplots()

colors = ['lightblue', 'gray', 'blue']

# ax.hist(x, n_bins, density=False, histtype='bar', stacked=True)
# ax.set_title('stacked bar')

ax.hist(x_multi, x_bins, density=False, histtype='bar', stacked=False,
        color=colors, label=['>8k ft','>6k ft','>3k ft'])
ax.set_title('Airfield Count by Range Bin and Rwy Length')
ax.set_xlabel('NM')
ax.legend(prop={'size': 10})

fig.tight_layout()
plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:04:01 2024

@author: andrew_s
"""

file = "/Users/andrew_s/Downloads/arctic240607/ARCTIC240607.shp"
import geopandas
df = geopandas.read_file(file)
df.plot(column="CT")
df.crs
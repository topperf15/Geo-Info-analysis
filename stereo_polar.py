#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 20:33:21 2024

@author: andrew_s
"""
import math

pi = math.pi
a = 6378137.0
e = 0.081819191

lat_o = pi/2
lon_o = 0
ko = 0.994
fe = 2000000
fn = 2000000
lat = 73
lon = 44
phi = lat*pi/180
gam = lon*pi/180

t = math.tan(pi/4-phi/2)*(((1+e*math.sin(phi))/(1-e*math.sin(phi)))**(e/2))
rho = 2*a*ko*t/((((1+e)**(1+e))*((1-e)**(1-e)))**0.5)

east = fe+rho*math.sin(gam-lon_o)
north = fn-rho*math.cos(gam-lon_o)
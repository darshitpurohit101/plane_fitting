#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:38:09 2021

@author: darshit
"""
#import open3d as o3d
import numpy as np
import pyransac3d as pyrsc

def plane(pts):
    #calling class Plane
    plane = pyrsc.Plane()
    parameters, inliners=plane.fit(pts, thresh=0.05, minPoints=100, maxIteration=1000)
    return parameters, inliners, pts
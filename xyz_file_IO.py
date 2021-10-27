# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:01:30 2021

@author: 91820
"""

# filename = "G:\\ELTE SEM-2\\3d computer vision\\PointClouds\\Tunnel.xyz"
# xyz = open(filename, "r")
# for lines in xyz:
#     # print(lines)
#     x, y, z = lines.split()
# # print(line)
# # line.split()
# # x, y, z = line.split()

# xyz.close()

import open3d as o3d
import numpy as np

sample_pcd = o3d.io.read_point_cloud("G:\\ELTE SEM-2\\3d computer vision\\PointClouds\\Tunnel.xyz")
ar = np.asarray(sample_pcd.points)
print(ar)
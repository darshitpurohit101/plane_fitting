# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:12:40 2021

@author: 91820
"""
import numpy 
from plyfile import PlyData, PlyElement

face = numpy.array([([0, 1, 2], 255, 255, 255),
                    ([0, 2, 3], 255,   0,   0),
                    ([0, 1, 3],   0, 255,   0),
                    ([1, 2, 3],   0,   0, 255)],
                   dtype=[('vertex_indices', 'i4', (3,)),
                          ('red', 'u1'), ('green', 'u1'),
                          ('blue', 'u1')])

el = PlyElement.describe(face, 'some_name', val_types={'some_property': 'f8'},
                          len_types={'some_property': 'u4'})

with open('test.ply', mode='wb') as f:
    PlyData([el], text=True).write(f)   
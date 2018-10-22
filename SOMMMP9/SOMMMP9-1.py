#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 12:44:33 2018
@author: mpcr
"""

##self-organizing map##
#DESeq2 data for MMP9 t-cell inhibititor conditions#

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import cv2
from scipy.misc import bytescale

filename = 'DE3.csv'
data = np.genfromtxt(filename, delimiter=',', missing_values='NA', filling_values=1, usecols=range(1,7))
print(data.shape)

genedata = np.genfromtxt(filename, dtype=str, delimiter=',', usecols=0)
print(genedata.shape)

for name in genedata:
    input = name
    input = input.lower()
    numbername = []
    for character in input:
        number = ord(character)
        numbername.append(number)
        print(numbername)
        #for number in numbername:
            #np.concatenate((number), axis=1)
            #print(numbername)

remove = data[:,1] != 0
data = data[remove,:]
removeNA = data[:, -1] != 1
data = data[removeNA, :]

data = np.append(genedata, data)

testnum = int(0.1 * data.shape[0])
randtestind = np.random.randint(0,data.shape[0], testnum)
testdata = data[randtestind, :]

data = np.delete(arr=data, obj=randtestind, axis= 0)

data -= np.mean(data, 0)
data /= np.std(data, 0)

n_in = data.shape[1]

w = np.random.randn(3, n_in) * 0.1

lr = 0.01
n_iters = 10000

for i in range(n_iters):
    randsamples = np.random.randint(0, data.shape[0], 1)[0] 
    rand_in = data[randsamples, :] 
    difference = w - rand_in
    dist = np.sum(np.absolute(difference), 1)
    best = np.argmin(dist)
    w_eligible = w[best,:]
    w_eligible += (lr * (rand_in - w_eligible))
    w[best,:] = w_eligible
    cv2.namedWindow('weights', cv2.WINDOW_NORMAL)
    cv2.imshow('weights', bytescale(w))
    cv2.waitKey(100)

node1w = w[0, :]
node2w = w[1, :]
node3w = w[2, :]
difference1 = node1w - testdata
dist1 = np.sum(np.absolute(difference1), 1)
difference2 = node2w - testdata
dist2 = np.sum(np.absolute(difference2), 1)
difference3 = node3w - testdata
dist3 = np.sum(np.absolute(difference3), 1)

#convert queried gene-number-name back into gene-letter-name
chr(ord('x'))

print (filename)
print (w)

    
    
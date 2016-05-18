# -*- coding: utf-8 -*-
"""
Physarum Polycephalum
Evaluation Main Script
Dynamic and Structur Analyzation
"""

#------------------ Libraries ------------------#

import numpy as np #numeric calculations
import matplotlib.pyplot as plt #figures and plots
#from PIL import Image as img #image objects
import slimetools as st #own functions defined in slimetools.py
import scipy.ndimage as ndimg #image tools filters and more
import os #read and navigate filesystem
import json


#------------------ Parameter ------------------#

offset = 200 #offset for threshold to seperate object from near noises
gaussian = 2 #sigma in 2D for gaussian filter before binarization
medianblock = 5 # m x m pixel block for median blurr filter (3,5)
usefilter = 'median' # filter for binarization ('gauss', 'median', 'none')
singleimagepath = 'fourth.tif' # path to single image for debugging
datapath = 'data_test' # relativ path to directory containing the .tif files
pxarea = 1 #area of 1px (depends on cam and optical setup)
bitnorm = 2**(-16) # value/bitnorm for display in common 8bit greyscale image


#------------------ Main ------------------#
"""
Single File
"""
"""
#general
image = plt.imread(singleimagepath) #reads image as array
fft = np.fft.fft2(image) #2D fourier transformed image
filtered = st.smooth(image, usefilter, gaussian, medianblock)#filter functions

#binarization
grad = st.grey2grad(image) #creates x-y-gradient from image array
limit = st.grad2threshold(filtered,grad) #returns threshold for this image
binary = st.grey2bin(filtered,limit-offset) #returns a binary array
binary_false = np.logical_not(binary) #invert logic make object true
filled = ndimg.binary_fill_holes(binary_false) #fill holes in object and dirt
labels, count = ndimg.measurements.label(filled) #numerate areas and count them
size = np.bincount(labels.ravel()) #apearance of each number, ravel makes 1D
biggest_label = size[1:].argmax() + 1 #size[0]=background, number=index+1
binary_final = biggest_label == labels #mask makes only biggest area true
area = sum(binary_final)*pxarea #sum over all entries = number of pixels
com = ndimg.measurements.center_of_mass(binary_final)

#contour
contour=st.find_contour(binary_final) #pixel coords with >=1 false neighbours

#kymograph 
kymograph = st.kymograph(image, com, 120, 0)
"""

"""
All Files
"""
dataList=[]
#dataList[img1,2,3,...][area<float>,center<array,float>,coords<array2d,int>]
for file in os.listdir(datapath):
    if file.endswith('.tif'):
        image = plt.imread(os.path.join('data',file)) #path cross platform
        filtered = st.smooth(image, usefilter, gaussian, medianblock)
        binary = st.binarify(image) #binary: threshold, fill, remove specks
        area = sum(sum(binary))*pxarea #number of pixels*area of one pixel
        com = ndimg.measurements.center_of_mass(binary) #center of mass coords
        contour=st.find_contour(binary) #pixel coords with false in 3x3
        dataList.append([area,com,contour])

dataList_json = json.dumps(dataList)
#------------------ Output ------------------#

"""
#Hier ist eine Änderung von Benjamin

#binarization
bin_figure= plt.figure()
plt.subplot(231)
image_pic = plt.imshow(image, cmap='pink')
plt.subplot(232)
fft_pic = plt.imshow(st.fft2display(fft), cmap='pink')
plt.subplot(233)
filtered_pic = plt.imshow(filtered, cmap='pink')
plt.plot(contour[:,1],contour[:,0],linestyle='none',marker='.',color='red')
plt.subplot(234)
binary_pic = plt.imshow(binary, cmap='pink')
plt.subplot(235)
filled_pic = plt.imshow(binary_final, cmap='pink')
center = plt.plot(com[0],com[1],marker='o', color='red')


#kymograph
kymo_figure= plt.figure()
plt.subplot(211)
plt.imshow(image, cmap='pink')
plt.plot((com[0],com[0]+120),(com[1],com[1]), color='r', linewidth='2')
plt.subplot(212)
plt.plot(np.arange(len(kymograph)),kymograph, color='r')
"""

print('done')



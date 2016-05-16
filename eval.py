# -*- coding: utf-8 -*-
"""
Physarum Polycephalum
Evaluation Main Script
Dynamic and Structur Analyzation
"""

#------------------ Libraries ------------------#

import numpy as np #numeric calculations
import matplotlib.pyplot as plt #figures and plots
from PIL import Image as img #image objects
import slimetools as st #own functions defined in slimetools.py
import scipy.ndimage as ndimg #image tools like gaussian filter
import cv2

#------------------ Parameter ------------------#

offset = 100 #offset for threshold to seperate object from near noises
gaussian = 2 #sigma in 2D for gaussian filter before binarization
medianblock = 5 # m x m pixel block for median blurr filter (3,5)
usefilter = 'median' # filter for binarization ('gauss', 'median', 'none')
singleimagepath = 'first.tif' # path to single image for debug

#------------------ Main ------------------#

#binarization
image = plt.imread(singleimagepath) #reads image as array
fft = np.fft.fft2(image) #2D fourier transformed image
filtered = st.smooth(image, usefilter, gaussian, medianblock)
grad = st.grey2grad(image) #creates x-y-gradient from image array
limit = st.grad2threshold(filtered,grad) #returns threshold for this image
binary = st.grey2bin(filtered,limit-offset) #returns a binary array
binary_false = np.logical_not(binary) #invert logic make object true
filled = ndimg.binary_fill_holes(binary_false) #fill holes in object and dirt
labels, count = ndimg.measurements.label(filled) #numerate areas and count them
#find biggest area
size = np.bincount(labels.ravel()) #apearance of each number, ravel makes 1D
biggest_label = size[1:].argmax() + 1 #size[0]=background, number=index+1
binary_final = biggest_label == labels #mask makes only biggest area true


#------------------ Output ------------------#

figure1 = plt.figure()
plt.subplot(231)
image_pic = plt.imshow(image, cmap='pink')
plt.subplot(232)
binary_pic = plt.imshow(binary, cmap='pink')
plt.subplot(233)
fft_pic = plt.imshow(st.fft2display(fft), cmap='pink')
plt.subplot(234)
filtered_pic = plt.imshow(filtered, cmap='pink')
plt.subplot(235)
filled_pic = plt.imshow(binary_final, cmap='pink')
print('done')
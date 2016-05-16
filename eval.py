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

#------------------ Parameter ------------------#
threshold_offset = -100
#------------------ Main ------------------#

image = plt.imread('first.tif') #reads image as array


fft = np.fft.fft2(image)
image_fft = fft
image_fft[0,0]=0
image_fft=np.abs(np.fft.fftshift(fft))

filtered = ndimg.gaussian_filter(image, sigma=(1,1))
grad = st.grey2grad(image) #creates x-y-gradient from image array
limit = st.grad2threshold(image,grad) #returns threshold for this image
binary = st.grey2bin(image,limit) #returns a binary array


#------------------ Output ------------------#

figure1 = plt.figure()
plt.subplot(221)
image_pic = plt.imshow(image, cmap='pink')
plt.subplot(222)
binary_pic = plt.imshow(binary, cmap='pink')
plt.subplot(223)
fft_pic = plt.imshow(image_fft, cmap='pink')
plt.subplot(224)
filtered_pic = plt.imshow(filtered, cmap='pink')
print 'done'
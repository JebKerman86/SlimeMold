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


#------------------ Main ------------------#

image = plt.imread('first.tif') #reads image as array
grad = st.grey2grad(image) #creates x-y-gradient from image array
limit = st.grad2threshold(image,grad) #returns threshold for this image
binary = st.grey2bin(image,limit) #returns a binary array


#------------------ Output ------------------#
figure1 = plt.figure()
plt.subplot(121)
image_pic = plt.imshow(image, cmap='pink')
plt.subplot(122)
binary_pic = plt.imshow(binary, cmap='pink')
print 'done'
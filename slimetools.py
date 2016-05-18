# -*- coding: utf-8 -*-
"""
Physarum Polycephalum
Functions for Evaluation
Created on Thu Apr 28 10:59:11 2016
@author: Lukas & Benjamin
"""

#------------------ Libraries ------------------#

import numpy as np #numeric calculations
#import matplotlib.pyplot as plt #figures and plots
#from PIL import Image as img #image objects
import scipy.ndimage as ndimg #image tools like gaussian filter auch in PIL


#------------------ Functions ------------------#

def findCenter(imArray):
    """
    returns the center of an array as coords
    WARN: the coords are not INT in general
    """
    imShape = imArray.shape
    imCenter = np.array([imShape[0]/2,imShape[1]/2])
    return imCenter
    
def find_contour(binary):
    """
    returns a array of coords ((x1,y1),(x2,y2), ... ) of object pixels 
    with 1 or more background pixels in 3x3 neighbourhood. req: binary image
    """
    coords = [] #declare list with dynamic length
    #-2 length and +1 ignores pixel at the edge of image (doesnt matter)
    for i in np.arange(len(binary)-2)+1:
        for j in np.arange(len(binary[0])-2)+1:
            if binary[i][j]: #if pixel = object
            #if NOT one of 3x3=object == 1 or more neighbours are background
                if not (binary[i-1][j-1] 
                and binary[i-1][j]
                and binary[i][j-1]
                and binary[i+1][j]
                and binary[i][j+1]
                and binary[i+1][j+1]
                and binary[i+1][j-1]
                and binary[i-1][j+1]):
                    coords.append((i,j))
    coords=np.asarray(coords)
    return coords



def gauss2d(shape=(3,3),sigma=0.5): #not used actually
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma]) 
    """
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h
    
    
def binarify(image):
    """
    requires a greyscale image<array> and threshold-offset-parameter<int>
    transforms it to binary image using some analyzation and corrections.
    create threshold via x,y-gradient: T=sum(img_ij*grad_ij)/sum(grad_ij)
    """
    gradient = grey2grad(image) #image gradient
    # T=top/bot
    bot=np.sum(gradient) #sum all elemts of gradient
    top=0 #init numerator for loop
    for i in range(image.shape[0]): #sum over all lines
        top+=np.dot(image[i],gradient[i]) #add inner product of each line
    limit=top/bot #calc the limit T
    binary=np.greater(image,limit)
    binary_false = np.logical_not(binary) #invert logic make object true
    filled = ndimg.binary_fill_holes(binary_false) #fill holes in object and dirt
    labels, count = ndimg.measurements.label(filled) #numerate areas and count them
    size = np.bincount(labels.ravel()) #apearance of each number, ravel makes 1D
    biggest_label = size[1:].argmax() + 1 #size[0]=background, number=index+1
    binary_final = biggest_label == labels #mask makes only biggest area true
    return binary_final
    
    
    
def grey2grad(im_array): #used from binarify
    """
    returns x and y gradient for given 2D <np.array>.
    Tested: Order of x- and y-gradient doesnt matter.
    d/dy(d/dx)==d/dx(d/dy)
    """
    #shape gives resolution of the array/image like [580,768]
    gradX = np.zeros(np.shape(im_array)) #init array with image resolution
    gradY = np.zeros(np.shape(im_array)) #init another for y-gradient
    #first build gradient from each line:
    for i,line in enumerate(im_array):
        gradX[i]=np.gradient(line)
    #than build gradient from the collumns of the first gradient d/dy(d/dx)
    for i in range(np.shape(im_array)[1]):
        gradY[:,i]=np.gradient(gradX[:,i])
    grad=np.abs(gradY) #absolute value of gradient_xy
    return grad


def grad2threshold(image,gradient): #in binarify
    """ 
    creates threshold for given grey-scale 
    image<array> and its gradient<array> in x and y direction.
    image and gradient must have same size.
    T=sum(image_ij*gradient_ij)/sum(gradient_ij)
    """        
    bot=np.sum(gradient) #sum all elemts of gradient
    top=0 #init numerator for loop
    for i in range(image.shape[0]): #loop lines
        #add the inner product of a line from image and gradient:
        top+=np.dot(image[i],gradient[i]) 
    treshold=top/bot #calc the fraction
    return treshold
    
    
def grey2bin(nparray, limit): #in binarify
    """transforms an array to booleans-array depending on the given limit"""
    bins = np.greater(nparray,limit)
    return bins




    
def smooth(image, usefilter, gaussian, medianblock):
    """
    filters given image <array> by given parameter usefilter <string>
    possible filters: gauss, median, none
    returns array
    """
    if usefilter=='gauss':
        filtered = ndimg.gaussian_filter(image, sigma=(gaussian,gaussian))
    elif usefilter=='median':
        filtered = ndimg.filters.median_filter(image, size=medianblock)
        #filtered = cv2.medianBlur(img, medianblock)
    elif usefilter=='none':
        filtered = image
    else: 
        print('no filter '+usefilter+' available. Use gauss, median or none')
        filtered = image #to avoid error
    return filtered
        
        
  
def kymograph(imArray,start,r,phi):
    """
    requiers <np.array>
    origin on top left pixel of the image (y-axe)
        #add the inner product of a line from image and gradient:
        #add the inner product of a line from image and gradient:
    Input: radius r(px)<int>, angle phi(deg)<fload>
    """
    stepSize = 1 #changed to 1
    numberOfSteps = r/stepSize #should be int
    phi = phi * (2.0*np.pi) / 360.0 #transform to deg->rad
    imDirection = np.array([np.cos(phi),-np.sin(phi)])*stepSize #step direction
    imSlice = [] #declare list
    for t in range(0,int(numberOfSteps)): #get for each step value from next px
        imCoords = start + imDirection*t #current position
        imCoords_round = np.round(imCoords,decimals=0) #round for next pixel
        imSlice.append(imArray[int(imCoords_round[0]),int(imCoords_round[1])])
    imSlice=np.asarray(imSlice) #transform the list to numeric array
    return imSlice


def fft2display(fft):
    """
    transforms a complex fourier transformed 2D array to displayable image
    removes the first entry and use fftshift + abs()
    returns displayable array
    """
    array=fft
    array[0,0]=0
    array=np.abs(np.fft.fftshift(array))
    return array
    


    

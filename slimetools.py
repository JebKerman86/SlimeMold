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
    
def gauss2d(shape=(3,3),sigma=0.5):
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
    
def grey2grad(im_array):
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


def grad2threshold(image,gradient):
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
    
    
def grey2bin(nparray, limit):
    """transforms an array to booleans-array depending on the given limit"""
    bins = np.greater(nparray,limit)
    return bins


def readColorImage(path):
    """
    returns Image object from PythonImageLibrary 
    and a Numpyarray with average rgba from given relativ path <String>
    """
    im_obj = img.open(path) #open image file
    im_array = np.mean(im_obj, axis=2) #average != 'real' grey value
    return im_obj, im_array
    
    
def readGreyImage(path):
    """
    maybe no need cause of plt.imageread() seems to do the same.
    returns (Image object from PythonImageLibrary 
    and) a Numpyarray with greyscales from given relativ path <String>
    """
    im_obj = img.open(path) #open image file
    im_array = np.array(im_obj) #image as array (for color[row[pix[r,g,b]]])
    #if np.array dim 3 print error
    #im_grey = np.mean(im_color, axis=2) #durchschnitt nicht "echter" grauwert
    return im_array
    
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
        filtered = image #to avoid bugs
    return filtered
            
            

def kymograph(imArray,start,r,phi):
    """
    requiers <np.array>
    origin on top left pixel of the image (y-axe)
    Input: radius r(px)<int>, angle phi(deg)<fload>
    """
    stepSize = 1 #changed to 1
    numberOfSteps = r/stepSize
    phi = phi * (2.0*np.pi) / 360.0
    imDirection = np.array([np.cos(phi),-np.sin(phi)])*stepSize
    imSlice = []    
    imCoords_round_previous = [-1,-1]
    for t in range(0,int(numberOfSteps)):
        imCoords = start + imDirection*t
        imCoords_round = np.round(imCoords,decimals=0)
        if (np.array_equiv(imCoords_round,imCoords_round_previous) == False 
        and imCoords_round[0] > 0 and imCoords_round[1] > 0):
            #print(imCoords_round)
            imSlice.append(imArray[imCoords_round[0],imCoords_round[1]])
            imCoords_round_previous = imCoords_round
             
    numberOfPixels = len(imSlice)
    #print("NumberOfPixels:  " + str(numberOfPixels))
    if(numberOfPixels != 0):
        avgPixelDist = r/(numberOfPixels-1)
    else:
        avgPixelDist = 0
    return [imSlice,avgPixelDist]


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
    


    

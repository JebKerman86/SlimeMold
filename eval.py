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
#import slimetools as st #own functions defined in slimetools.py


#------------------ Main ------------------#


#------------------ Output ------------------#
image = img.open("try.tif")
image_arr = np.array(image)
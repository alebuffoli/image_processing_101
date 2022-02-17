import skimage.io
import skimage.color
import numpy as np
import matplotlib
import sys
import matplotlib.pyplot as plt
import platform
if platform.system() == 'Darwin':
    matplotlib.use('TkAgg')
import skimage.filters
import sys


"""
    Lesson available here -> https://datacarpentry.org/image-processing/06-blurring/index.html

    ---------------------------------------------

    ############ Blurring Images ############
"""

image = skimage.io.imread(fname='data/gaussian-original.png')

sigma = 7.0

blurred = skimage.filters.gaussian(
    image, sigma=(sigma, sigma), truncate=3.5, multichannel=True)
skimage.io.imshow(blurred)
plt.show()
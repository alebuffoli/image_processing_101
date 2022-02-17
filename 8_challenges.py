import skimage.io
import skimage.color
import skimage.filters
import skimage.measure

import numpy as np
import matplotlib
import sys
import matplotlib.pyplot as plt
import platform
if platform.system() == 'Darwin':
    matplotlib.use('TkAgg')


def count_colonies(image_filename):
    bacteria_image = skimage.io.imread(image_filename)
    gray_bacteria = skimage.color.rgb2gray(bacteria_image)
    blurred_image = skimage.filters.gaussian(gray_bacteria, sigma=1.0)
    mask = blurred_image < 0.2
    labeled_image, count = skimage.measure.label(mask, return_num=True)
    print(f"There are {count} colonies in {image_filename}")

    colored_label_image = skimage.color.label2rgb(labeled_image, bg_label=0)
    summary_image = skimage.color.gray2rgb(gray_bacteria)
    summary_image[mask] = colored_label_image[mask]
    fig, ax = plt.subplots()
    plt.imshow(summary_image)
    plt.show()


for image_filename in ["data/colonies-01.tif", "data/colonies-02.tif", "data/colonies-03.tif"]:
    count_colonies(image_filename)
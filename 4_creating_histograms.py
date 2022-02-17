import skimage.io
import skimage.color
import numpy as np
import matplotlib
import random
import sys
import matplotlib.pyplot as plt
import platform
if platform.system() == 'Darwin':
    matplotlib.use('TkAgg')


"""
    Lesson available here -> https://datacarpentry.org/image-processing/05-creating-histograms/index.html

    ---------------------------------------------

    ############ Creating Histograms ############
"""

# image = skimage.io.imread(fname='data/plant-seedling.jpg', as_gray=True)
#
# histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
#
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("grayscale value")
# plt.ylabel("pixel count")
# plt.xlim([0.0, 1.0])  # <- named arguments do not work here
#
# plt.plot(bin_edges[0:-1], histogram)  # <- or here
# plt.show()


"""
    ############ Color Histograms ############
"""


# image = skimage.io.imread('data/plant-seedling.jpg')
#
# # tuple to select colors of each channel line
# colors = ("red", "green", "blue")
# channel_ids = (0, 1, 2)
#
# # create the histogram plot, with three lines, one for
# # each color
# plt.figure()
# plt.xlim([0, 256])
# for channel_id, c in zip(channel_ids, colors):
#     histogram, bin_edges = np.histogram(
#         image[:, :, channel_id], bins=256, range=(0, 256)
#     )
#     plt.plot(bin_edges[0:-1], histogram, color=c)
#
# plt.title("Color Histogram")
# plt.xlabel("Color value")
# plt.ylabel("Pixel count")
#
# plt.show()


"""
    ############ Color histogram with a mask ############
"""

image = skimage.io.imread('data/wellplate-02.tif')

# create a circular mask to select the 7th well in the first row
mask = np.zeros(shape=image.shape[0:2], dtype="bool")
circle = skimage.draw.disk((240, 1053), radius=49, shape=image.shape[0:2])
mask[circle] = 1

# just for display:
# make a copy of the image, call it masked_image, and
# use np.logical_not() and indexing to apply the mask to it
masked_img = image[:]
masked_img[np.logical_not(mask)] = 0

# create a new figure and display masked_img, to verify the
# validity of your mask
fig, ax = plt.subplots()
plt.imshow(masked_img)
plt.show()

# list to select colors of each channel line
colors = ("red", "green", "blue")
channel_ids = (0, 1, 2)

# create the histogram plot, with three lines, one for
# each color
plt.figure()
plt.xlim([0, 256])
for (channel_id, c) in zip(channel_ids, colors):
    # use your circular mask to apply the histogram
    # operation to the 7th well of the first row
    histogram, bin_edges = np.histogram(
        image[:, :, channel_id][mask], bins=256, range=(0, 256)
    )

    plt.plot(histogram, color=c)

plt.xlabel("color value")
plt.ylabel("pixel count")

plt.show()


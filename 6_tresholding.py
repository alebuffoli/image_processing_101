import skimage.io
import skimage.color
import skimage.filters
import numpy as np
import matplotlib
import sys
import matplotlib.pyplot as plt
import platform
if platform.system() == 'Darwin':
    matplotlib.use('TkAgg')
import skimage.filters
import glob

"""
    Lesson available here -> https://datacarpentry.org/image-processing/07-thresholding/index.html

    ---------------------------------------------

    ############ Thresholding ############
"""


# image = skimage.io.imread("data/shapes-01.jpg")
#
# # convert the image to grayscale
# gray_image = skimage.color.rgb2gray(image)
#
# # blur the image to denoise
# blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
#
# # Create histogram to determine where to set the threshold
# histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))
#
# plt.plot(bin_edges[0:-1], histogram)
# plt.title("Grayscale Histogram")
# plt.xlabel("grayscale value")
# plt.ylabel("pixels")
# plt.xlim(0, 1.0)
# plt.show()
#
# # create a mask based on the threshold
# threshold = 0.8
# binary_mask = blurred_image < threshold
#
# fig, ax = plt.subplots()
# plt.imshow(binary_mask, cmap='gray')
# plt.show()
#
# selection = np.zeros_like(image)
# selection[binary_mask] = image[binary_mask]
#
# fig, ax = plt.subplots()
# plt.imshow(selection)
# plt.show()


"""
    ############ Exercise ############
"""


# image = skimage.io.imread("data/shapes-02.jpg")
#
# # convert the image to grayscale
# gray_image = skimage.color.rgb2gray(image)
#
# # blur the image to denoise
# blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
#
# # Create histogram to determine where to set the threshold
# histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))
#
# plt.plot(bin_edges[0:-1], histogram)
# plt.title("Grayscale Histogram")
# plt.xlabel("grayscale value")
# plt.ylabel("pixels")
# plt.xlim(0, 1.0)
# plt.show()
#
# # create a mask based on the threshold
# threshold = 0.5
# binary_mask = blurred_image > threshold
#
# fig, ax = plt.subplots()
# plt.imshow(binary_mask, cmap='gray')
# plt.show()
#
# selection = np.zeros_like(image)
# selection[binary_mask] = image[binary_mask]
#
# fig, ax = plt.subplots()
# plt.imshow(selection)
# plt.show()


"""
    ############ Automatic thresholding ############
"""

# image = skimage.io.imread("data/maize-root-cluster.jpg")
#
# # convert the image to grayscale
# gray_image = skimage.color.rgb2gray(image)
#
# # blur the image to denoise
# blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
#
# # show the histogram of the blurred image
# histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))
# plt.plot(bin_edges[0:-1], histogram)
# plt.title("Graylevel histogram")
# plt.xlabel("gray value")
# plt.ylabel("pixel count")
# plt.xlim(0, 1.0)
# plt.show()
#
# # Search for the threshold automatically
# threshold = skimage.filters.threshold_otsu(blurred_image)
# print('Threshold: ', threshold)
# binary_mask = blurred_image > threshold
#
# # apply the binary mask to select the foreground
# selection = np.zeros_like(image)
# selection[binary_mask] = image[binary_mask]
#
# fig, ax = plt.subplots()
# plt.imshow(selection)
# plt.show()



"""
    ############ Application: measuring root mass ############
"""


# def enhanced_root_mass(filename, sigma):
#
#     # read the original image, converting to grayscale on the fly
#     image = skimage.io.imread(fname=filename, as_gray=True)
#
#     # blur before thresholding
#     blurred_image = skimage.filters.gaussian(image, sigma=sigma)
#
#     # perform inverse binary thresholding to mask the white label and circle
#     binary_mask = blurred_image > 0.95
#
#     # use the mask to remove the circle and label from the blurred image
#     blurred_image[binary_mask] = 0
#
#     # perform automatic thresholding to produce a binary image
#     t = skimage.filters.threshold_otsu(blurred_image)
#     binary_mask = blurred_image > t
#
#     skimage.io.imshow(binary_mask)
#     plt.show()
#
#     # determine root mass ratio
#     rootPixels = np.count_nonzero(binary_mask)
#     w = binary_mask.shape[1]
#     h = binary_mask.shape[0]
#     density = rootPixels / (w * h)
#
#     return density
#
#
# root = enhanced_root_mass("data/trial-016.jpg", sigma=1.5)
# print(root)


"""
    ############ Thresholding a bacteria colony image ############
"""


# read the original image, converting to grayscale on the fly
image = skimage.io.imread(fname='data/colonies-01.tif', as_gray=True)


# blur before thresholding
blurred_image = skimage.filters.gaussian(image, sigma=1.5)

# show the histogram of the blurred image
histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))
plt.plot(bin_edges[0:-1], histogram)
plt.title("Graylevel histogram")
plt.xlabel("gray value")
plt.ylabel("pixel count")
plt.xlim(0, 1.0)
plt.show()

binary_mask = blurred_image < 0.2

fig, ax = plt.subplots()
skimage.io.imshow(image)
fig, ax = plt.subplots()
skimage.io.imshow(binary_mask)
plt.show()
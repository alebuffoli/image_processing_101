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



"""
    Lesson available here -> https://datacarpentry.org/image-processing/08-connected-components/index.html

    ---------------------------------------------

    ############ Connected Component Analysis ############
"""


def connected_components(filename, sigma=1.0, t=0.5, connectivity=2):
    # load the image
    image = skimage.io.imread(filename)
    # convert the image to grayscale
    gray_image = skimage.color.rgb2gray(image)
    # denoise the image with a Gaussian filter
    blurred_image = skimage.filters.gaussian(gray_image, sigma=sigma)
    # mask the image according to threshold
    binary_mask = blurred_image < t
    # perform connected component analysis
    labeled_image, count = skimage.measure.label(binary_mask,
                                                 connectivity=connectivity, return_num=True)
    return labeled_image, count


# labeled_image, count = connected_components("data/shapes-01.jpg", sigma=3.0, t=0.9, connectivity=2)
#
# print(count)
# print("dtype:", labeled_image.dtype)
# print("min:", np.min(labeled_image))
# print("max:", np.max(labeled_image))
# colored_label_image = skimage.color.label2rgb(labeled_image, bg_label=0)
#
# fig, ax = plt.subplots()
# plt.imshow(colored_label_image)
# plt.axis('off')
# plt.show()



"""
    ############ Morphometrics - Describe object features with numbers ############
"""


labeled_image, count = connected_components("data/shapes-01.jpg", sigma=1.0, t=0.9, connectivity=2)
object_features = skimage.measure.regionprops(labeled_image)
object_areas = [objf["area"] for objf in object_features]
print(object_areas)

min_area = 150
object_areas = np.array([objf["area"] for objf in object_features])
object_labels = np.array([objf["label"] for objf in object_features])
large_objects = object_labels[object_areas > min_area]
print("Found", len(large_objects), "objects!")


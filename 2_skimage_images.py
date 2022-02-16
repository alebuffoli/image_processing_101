import skimage.io
import skimage.color

import matplotlib
import sys
import matplotlib.pyplot as plt
import skimage.transform
import platform
if platform.system() == 'Darwin':
    matplotlib.use('TkAgg')

"""
    Lesson available here -> https://datacarpentry.org/image-processing/03-skimage-images/index.html

    ---------------------------------------------

    ############ Reading and displaying ############
"""

# # read image
# image = skimage.io.imread(fname="data/chair.jpg")
# skimage.io.imshow(image)
# plt.show()


"""
    ############ Saving images ############
"""

# image = skimage.io.imread(fname="data/chair.jpg")
# skimage.io.imshow(image)
#
# # save a new version in .tif format
# skimage.io.imsave(fname="data/chair.tif", arr=image)


"""
    ############ Exercise, Resizing images ############
"""

# image = skimage.io.imread(fname="data/chair.jpg")
# new_shape = (image.shape[0] // 10, image.shape[1] // 10, image.shape[2])
# small = skimage.transform.resize(image=image, output_shape=new_shape)
# small = skimage.img_as_ubyte(small)
#
# skimage.io.imsave(fname="data/resized.jpg", arr=small)
#
#
# fig, ax = plt.subplots()
# plt.imshow(image)
# fig, ax = plt.subplots()
# plt.imshow(small)
# plt.show()


"""
    ############ Manipulating pixels ############
    
    Run this program in the shell with:
    `python3 2_skimage_images.py data/maize-root-cluster.jpg`
"""


# # read input image, based on filename parameter
# image = skimage.io.imread(fname=sys.argv[1])
# print(image)
#
# # display original image
# skimage.io.imshow(image)
#
# # keep only high-intensity pixels
# image[image < 128] = 0
#
# # display modified image
# skimage.io.imshow(image)
# plt.show()

"""
    ############ Exercise, low intensity pixels  ############

    Run this program in the shell with:
    `python3 2_skimage_images.py data/sudoku.png`
"""

# # read input image, based on filename parameter
# image = skimage.io.imread(fname=sys.argv[1])
#
# # display original image
# skimage.io.imshow(image)
#
# # keep only high-intensity pixels
# print(image[0][0])
# image[image == 255] = 64
# print(image[0][0])
#
# # display modified image
# skimage.io.imshow(image)
# plt.show()


"""
    ############ Converting color images to grayscale ############
    
     Run this program in the shell with:
    `python3 2_skimage_images.py data/maize-root-cluster.jpg`
"""

# # read input image, based on filename parameter
# image = skimage.io.imread(fname=sys.argv[1])
#
# # display original image
# skimage.io.imshow(image)
#
# # convert to grayscale and display
# gray_image = skimage.color.rgb2gray(image)
# skimage.io.imshow(gray_image)
# plt.show()


"""
    ############ Grayscale as argument ############
    
     Run this program in the shell with:
    `python3 2_skimage_images.py data/maize-root-cluster.jpg`
"""

# # read input image, based on filename parameter
# image = skimage.io.imread(fname=sys.argv[1], as_gray=True)
#
# # display grayscale image
# skimage.io.imshow(image)
# plt.show()


"""
    ############ Access Via Slicing ############
"""

# image = skimage.io.imread(fname="data/board.jpg")
#
# clip = image[60:151, 135:481, :]
# skimage.io.imshow(clip)
# skimage.io.imsave(fname="data/clip.tif", arr=clip)
# plt.show()


"""
    ############ Change color image on sliced part ############
"""

# image = skimage.io.imread(fname="data/board.jpg")
#
# color = image[330, 90]
# image[60:151, 135:481] = color
# skimage.io.imshow(image)
# plt.show()


"""
    ############ Exercise ############
"""


# # load and display original image
# image = skimage.io.imread(fname="data/maize-root-cluster.jpg")
#
# # extract and display the subclip
#
# clip = image[0:399, 300:500, :]
#
# fig, ax = plt.subplots()
# plt.imshow(image)
# fig, ax = plt.subplots()
# plt.imshow(clip)
# plt.show()
#
# # Save it
#
# skimage.io.imsave(fname="data/root-sliced.jpg", arr=clip)

"""
    ############ Exercise 2, Slicing and the colorimetric challenge ############
"""


def select_zone(image, y_f, y_t, x_f, x_t):
    # top
    image[y_f-1:y_f, x_f:x_t] = [255, 0, 0]
    # Left
    image[y_f-1:y_t+1, x_f-1:x_f] = [255, 0, 0]
    # bottom
    image[y_t:y_t+1, x_f:x_t] = [255, 0, 0]
    # Right
    image[y_f-1:y_t+1, x_t:x_t+1] = [255, 0, 0]
    return image


# # load and display original image
image = skimage.io.imread(fname="data/titration.tiff", plugin='pil')

y_f = 200
y_t = 240
x_f = 350
x_t = 390

# extract the subclip
clip = image[y_f:y_t, x_f:x_t, :]

# Draw the zone in the original image
image = select_zone(image, y_f, y_t, x_f, x_t)

red = 0
green = 0
blue = 0
pixels = 0

for x in clip:
    for y in x:
        pixels += 1
        red += y[0]
        green += y[1]
        blue += y[2]

print('Avg. red value: ', red / pixels)
print('Avg. green value: ', green / pixels)
print('Avg. blue value: ', blue / pixels)

# Shows up the original image and the clip
fig, ax = plt.subplots()
plt.imshow(image)
fig, ax = plt.subplots()
plt.imshow(clip)
plt.show()







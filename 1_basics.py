import numpy as np
import skimage.io
import skimage.viewer
import matplotlib
import matplotlib.pyplot as plt
import ipympl
import platform
if platform.system() == 'Darwin':
    matplotlib.use('TkAgg')


"""
    Lesson available here -> https://datacarpentry.org/image-processing/02-image-basics/index.html
    
    ---------------------------------------------
    
    ############ Working with Pixels ############
"""
image = skimage.io.imread(fname="data/eight.tif")
plt.imshow(image)
plt.show()

print(image.shape)
print(image)

"""
    ############ MAKE A ZERO ############
"""

# zero = skimage.io.imread(fname="data/eight.tif")
# zero[2, 1] = 1.0
#
# """
#     The follwing line of code creates a new figure for imshow to use
#     in displaying our output. Without it, plt.imshow() would overwrite
#     our previous image in the cell above
# """
# fig, ax = plt.subplots()
# plt.imshow(zero)
# plt.show()
# print(zero)

"""
    ############ EXERCISE | MAKE A FIVE ############
"""

# five = skimage.io.imread(fname="data/eight.tif")
# five[1, 2] = 1.0
# five[3, 0] = 1.0
# fig, ax = plt.subplots()
# plt.imshow(five)
# print(five)
# plt.show()


"""
    ############ More colors ############
"""
# make a copy of eight
# three_colors = skimage.io.imread(fname="data/eight.tif")
#
# # multiply the whole matrix by 128
# three_colors = three_colors * 128
#
# # set the middle row (index 2) to the value of 255., so you end up with the values 0.,128.,and 255
# three_colors[2, :] = 255.
# fig, ax = plt.subplots()
# plt.imshow(three_colors)
# print(three_colors)
# plt.show()

"""
    ############ Gray Scale ############
"""
# make a copy of eight
# three_colors = skimage.io.imread(fname="data/eight.tif")
#
# # multiply the whole matrix by 128
# three_colors = three_colors * 128
#
# # set the middle row (index 2) to the value of 255., so you end up with the values 0.,128.,and 255
# three_colors[2, :] = 255.
# fig, ax = plt.subplots()
# plt.imshow(three_colors, cmap=plt.cm.gray)
# print(three_colors)
# plt.show()

"""
    ############ Even More Colors ############
"""

# set the random seed so we all get the same matrix
# pseudorandomizer = np.random.RandomState(2021)
#
# # create a 4 X 4 checkerboard of random colors
# checkerboard = pseudorandomizer.randint(0, 255, size=(4, 4, 3))
# # restore the default map as you show the image
# fig, ax = plt.subplots()
# plt.imshow(checkerboard)
#
# # display the arrays
# print(checkerboard)
# plt.show()


"""
    ############ Even More Colors, extract info on blue square ############
"""
#
# # set the random seed so we all get the same matrix
# pseudorandomizer = np.random.RandomState(2021)
#
# # create a 4 X 4 checkerboard of random colors
# checkerboard = pseudorandomizer.randint(0, 255, size=(4, 4, 3))
# # restore the default map as you show the image
# fig, ax = plt.subplots()
# plt.imshow(checkerboard)
#
# # extract all the color information for the blue square
# upper_right_square = checkerboard[1, 3, :]
# print(upper_right_square)


"""
    ############ Even More Colors, Red Channel ############
"""

# # set the random seed so we all get the same matrix
# pseudorandomizer = np.random.RandomState(2021)
#
# # create a 4 X 4 checkerboard of random colors
# checkerboard = pseudorandomizer.randint(0, 255, size=(4, 4, 3))
#
# red_channel = checkerboard * [1, 0, 0]
# fig, ax = plt.subplots()
# plt.imshow(red_channel)
# plt.show()

"""
    ############ Even More Colors, Green Channel ############
"""

# # set the random seed so we all get the same matrix
# pseudorandomizer = np.random.RandomState(2021)
#
# # create a 4 X 4 checkerboard of random colors
# checkerboard = pseudorandomizer.randint(0, 255, size=(4, 4, 3))
#
# red_channel = checkerboard * [0, 1, 0]
# fig, ax = plt.subplots()
# plt.imshow(red_channel)
# plt.show()


"""
    ############ Even More Colors, Blue Channel ############
"""

# # set the random seed so we all get the same matrix
# pseudorandomizer = np.random.RandomState(2021)
#
# # create a 4 X 4 checkerboard of random colors
# checkerboard = pseudorandomizer.randint(0, 255, size=(4, 4, 3))
#
# red_channel = checkerboard * [0, 0, 1]
# fig, ax = plt.subplots()
# plt.imshow(red_channel)
# plt.show()
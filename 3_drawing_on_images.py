import skimage.io
import skimage.draw
import numpy as np
import matplotlib
import random
import sys
import matplotlib.pyplot as plt
import platform
if platform.system() == 'Darwin':
    matplotlib.use('TkAgg')



"""
    Lesson available here -> https://datacarpentry.org/image-processing/04-drawing/index.html

    ---------------------------------------------

    ############ Drawing on images ############
"""


# image = skimage.io.imread("data/maize-seedlings.tif")
#
# mask = np.ones(shape=image.shape[0:2], dtype="bool")
#
# rr, cc = skimage.draw.rectangle(start=(357, 44), end=(740, 720))
# mask[rr, cc] = False
#
# fig, ax = plt.subplots()
# plt.imshow(mask, cmap='gray')
# plt.show()


"""
    ############ Exercise ############
"""

# image = np.zeros(shape=(600, 800, 3), dtype="uint8")
#
# rr, cc = skimage.draw.disk((200, 300), 100, shape=image.shape[0:2])
# image[rr, cc] = (0, 0, 255)
#
# rr, cc = skimage.draw.line(400, 200, 500, 700)
# image[rr, cc] = (0, 255, 0)
#
# fig, ax = plt.subplots()
# plt.imshow(image, cmap='gray')
# plt.show()


"""
    ############ Exercise 2 ############
"""

# create the black canvas
# image = np.zeros(shape=(600, 800, 3), dtype="uint8")
#
# # draw a blue circle at a random location 15 times
# for i in range(15):
#     rr, cc = skimage.draw.disk((
#          random.randrange(600),
#          random.randrange(800)),
#          radius=50,
#          shape=image.shape[0:2],
#         )
#     image[rr, cc] = (0, 0, 255)
#
#
# # display the results
# fig, ax = plt.subplots()
# plt.imshow(image)
# plt.show()

"""
    ############ Understanding the next part ############
"""

# # Load an image of 2x2 px
# # |0 0|
# # |0 0|
# image = skimage.io.imread("data/3_drawing_4px.jpg")
# print('image: ', image)
# # image:
# # [[[114 116 115] [114 116 115]]
# #  [[114 116 115] [114 116 115]]]
#
#
# # Create the basic mask
# mask = np.ones(shape=image.shape[0:2], dtype="bool")
# print('mask: ', mask)
# # mask:
# # [[ True  True]
# #  [ True  True]]
#
#
# # Draw a square in the right corner of the image
# # |0 0|
# # |0 X| <-- here
# rr, cc = skimage.draw.rectangle(start=(1, 1), end=(1, 1))
# print('rr ', rr)
# print('cc ', cc)
# # rr:  [[1]]
# # cc:  [[1]]
#
# # Basically the rr and cc determinate where we didn't draw the square
# # here:
# # |X X|
# # |X 0|
#
#
# # Here now is pretty simple, we set False where we didn't draw the square
# mask[rr, cc] = False
# print('mask: ', mask)
# # mask:
# # [[ True  True]
# #  [ True False]]
#
# # Now we compare the image array with the mask array
# # where in the mask array we have True, we set in the image the RGB to Zero
# image[mask] = 0
# print('image: ', image)
# # image before:
# # [[[114 116 115] [114 116 115]]
# #  [[114 116 115] [114 116 115]]]
#
# # image after:
# # [[[  0   0   0] [  0   0   0]]
# #  [[  0   0   0] [114 116 115]]]
#
#
# fig, ax = plt.subplots()
# skimage.io.imshow(image)
# plt.show()

"""
    ############ Image modification ############
"""

# # Load the original image
# image = skimage.io.imread("data/maize-seedlings.tif")
#
# # Create the basic mask
# mask = np.ones(shape=image.shape[0:2], dtype="bool")
#
# # Draw a filled rectangle on the mask image
# rr, cc = skimage.draw.rectangle(start=(357, 44), end=(740, 720))
# mask[rr, cc] = False
#
# image[mask] = 0
#
# fig, ax = plt.subplots()
# skimage.io.imshow(image)
# plt.show()

"""
    ############ Exercise - Masking an image of your own ############
"""

# # Load the image
# image = skimage.io.imread("data/remote-control.jpg")
#
# mask = np.ones(shape=image.shape[0:2], dtype="bool")
#
# rr, cc = skimage.draw.rectangle(start=(65, 1100), end=(1850, 1680))
# mask[rr, cc] = False
#
# image[mask] = 0
#
# fig, ax = plt.subplots()
# skimage.io.imshow(image)
# plt.show()


"""
    ############ Exercise - Masking a 96-well plate image ############
"""


# Load the image
image = skimage.io.imread("data/wellplate-01.jpg")

wells = []
with open("data/centers.txt", "r") as center_file:
    for line in center_file:
        # ... getting the coordinates of each well...
        coordinates = line.split()
        x = int(coordinates[0])
        y = int(coordinates[1])
        wells.append([x, y])

mask = np.ones(shape=image.shape[0:2], dtype="bool")

for x in wells:
    rr, cc = skimage.draw.disk((x[1], x[0]), 16, shape=image.shape[0:2])

    mask[rr, cc] = False

image[mask] = 0


# Display the image
fig, ax = plt.subplots()
plt.imshow(image)
plt.show()

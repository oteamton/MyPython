from skimage.io import imread, imshow
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt

img = imread('Python/testimg5m.jpg')
# imshow(img)


hogfv , hog_image, = hog(img, orientations = 9, pixels_per_cell=(8,8),cells_per_block=(3,3),
visualize=True, channel_axis=-1)

hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0,5))

# show hog and original together
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.imshow(img)
ax1.set_title('Original Image')

ax2.imshow(hog_image_rescaled, cmap='gray')
ax2.set_title('HOG Image')

plt.show()

#Show ontop of original
# fig, ax = plt.subplots(figsize=(8, 4))

# ax.imshow(img)
# ax.imshow(hog_image_rescaled, cmap='jet', alpha=0.5)

# plt.show()
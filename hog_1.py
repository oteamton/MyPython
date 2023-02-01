from skimage.io import imread, imshow
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt

img = imread('testimg3.jpg')
imshow(img)


hogfv , hog_image, = hog(img, orientations = 9, pixels_per_cell=(16,16),cells_per_block=(2,2),
visualize=True, channel_axis=-1)

hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0,5))
# imshow(hog_image_rescaled)

plt.imshow(img)
plt.show()

plt.imshow(hog_image_rescaled, cmap='gray')
plt.show()


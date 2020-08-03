import cv2
import os

HOME_DIR = os.environ['HOME']

image = cv2.imread(HOME_DIR + "/data/StarterBundle/ch03/IMG_0140.JPG")

print(image.shape)

bgr = image[10, 100]
# blue, green, red ordering

print(bgr)

rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

print(rgb)

# cv2.imshow("Image", image)

# cv2.waitKey(0)

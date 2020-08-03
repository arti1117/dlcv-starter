import numpy as np
import cv2
import os

HOME_DIR = os.environ['HOME']

labels = ["dog", "cat", "panda"]
np.random.seed(1)

W = np.random.randn(3, 3072)
b = np.random.randn(3)

orig = cv2.imread(HOME_DIR + "/data/StarterBundle/ch08/puppy.jpg")
image = cv2.resize(orig, (32, 32)).ravel()
# image = cv2.resize(orig, (32, 32)).reshape((-1))

scores = W.dot(image) + b

for (label, score) in zip(labels, scores):
    print("[INFO] {}: {:.2f}".format(label, score))

cv2.putText(orig, "Label: {}".format(labels[np.argmax(scores)]),
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

cv2.imshow("Image", orig)
cv2.waitKey(2000)


import os
import matplotlib.pyplot as plt
import cv2
file_path = os.path.join('Background','image.png')
#with open(file_path, 'r') as file:
#content = file_path.read()
image = cv2.imread(file_path)
if image is not None:
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else: print('image not found')
def readImage(folder):
    pass
    return
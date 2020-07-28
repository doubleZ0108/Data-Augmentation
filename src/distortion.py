import numpy as np
import cv2
from PIL import Image
import shutil

'''
_distortion
    镜头畸变
    (需要重新手工标注)

    Lens distortion
    (Manual marking is needed again)
'''
def distortion(img):
    d_coef= np.array((0.15, 0.15, 0.1, 0.1, 0.05))

    # get the height and the width of the image
    h, w = img.shape[:2]

    # compute its diagonal
    f = (h ** 2 + w ** 2) ** 0.5

    # set the image projective to carrtesian dimension
    K = np.array([[f, 0, w / 2],
                  [0, f, h / 2],
                  [0, 0,   1  ]])

    d_coef = d_coef * np.random.random(5) # value
    d_coef = d_coef * (2 * (np.random.random(5) < 0.5) - 1) # sign

    # Generate new camera matrix from parameters
    M, _ = cv2.getOptimalNewCameraMatrix(K, d_coef, (w, h), 0)

    # Generate look-up tables for remapping the camera image
    remap = cv2.initUndistortRectifyMap(K, d_coef, None, M, (w, h), 5)

    # Remap the original image to a new image
    distortion_img = cv2.remap(img, *remap, cv2.INTER_LINEAR)

    return Image.fromarray(np.uint8(distortion_img))
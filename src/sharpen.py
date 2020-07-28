import numpy as np
import cv2
from PIL import Image
import shutil

'''
_sharpen
    图像锐化
    Image sharpening
'''
def sharpen(img):
    img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)

    identity = np.array([[0, 0, 0],
                        [0, 1, 0],
                        [0, 0, 0]])
    sharpen = np.array([[ 0, -1,  0],
                        [-1,  4, -1],
                        [ 0, -1,  0]]) / 4
    max_center = 4

    sharp = sharpen * np.random.random() * max_center
    kernel = identity + sharp

    sharpen_img = cv2.filter2D(img, -1, kernel)
    return Image.fromarray(cv2.cvtColor(sharpen_img,cv2.COLOR_BGR2RGB))

def saveSharpenLabel(name):
    shutil.copyfile(name + ".txt", name + "_sharpen.txt")
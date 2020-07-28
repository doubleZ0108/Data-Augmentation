import numpy as np
import cv2
from PIL import Image
import shutil

'''
_contrast
    对比度变换
    Contrast transformation
'''
def contrast(img):
    img = Image.fromarray(img)
    range_contrast=(-50, 50)

    contrast = np.random.randint(*range_contrast)

    contrast_img = img.point(lambda p: p * (contrast / 127 + 1) - contrast)

    return Image.fromarray(np.uint8(contrast_img))

def saveContrastLabel(name):
    shutil.copyfile(name + ".txt", name + "_contrast.txt")
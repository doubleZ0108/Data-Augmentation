import numpy as np
import cv2
from PIL import Image
import shutil

'''
_blur
    高斯模糊
    Gaussian Blur
'''
def blur(img):
    img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)

    kernel_size = (7, 7)
    blur_img = cv2.GaussianBlur(img,kernel_size,0)

    return Image.fromarray(cv2.cvtColor(blur_img,cv2.COLOR_BGR2RGB))

def saveBlurLabel(name):
    shutil.copyfile(name + ".txt", name + "_blur.txt")
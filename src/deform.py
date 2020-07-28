import numpy as np
import cv2
from PIL import Image
import shutil

'''
_deform
    图像拉伸
    拉伸成长宽为原始宽的正方形图像
    (需要重新手工标注)

    A square image stretched to its original width
    (Manual marking is needed again)
'''
def deform(img):
    img = Image.fromarray(img)
    w, h = img.size[:2]

    # 拉伸成宽为w的正方形
    deform_img = img.resize((int(w), int(w)))

    return deform_img
    

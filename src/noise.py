# coding=utf-8
from PIL import Image
import numpy as np
import shutil
import os

'''
_noise
    为图像添加噪声
    随机生成5000个椒盐
    
    Add noise to the image
    Randomly generate 5,000 salt and pepper
'''
def addNoise(img):
    rows,cols,dims = img.shape
    noise_img = img
    for i in range(5000):
        x = np.random.randint(0,rows)
        y = np.random.randint(0,cols)
        noise_img[x,y,:] = 255
    noise_img.flags.writeable = True  # 将数组改为读写模式

    return Image.fromarray(np.uint8(noise_img))

def saveNoiseLabel(name):
    shutil.copyfile(name + ".txt", name + "_noise.txt")
import numpy as np
import cv2
from PIL import Image
import shutil

'''
_brightness
    图像亮度增强
    Image brightness enhancement
'''
def brightness(img):
    img = Image.fromarray(img)

    brightness = 1 + np.random.randint(1, 9) / 10
    brightness_img = img.point(lambda p: p * brightness)

    return Image.fromarray(np.uint8(brightness_img))

def saveBrightnessLabel(name):
    shutil.copyfile(name + ".txt", name + "_brightness.txt")

'''
_darkness
    图像亮度降低
    Image brightness reduction
'''
def darkness(img):
    darkness = np.random.randint(1, 9) / 10
    darkness_img = img * darkness
    return Image.fromarray(np.uint8(darkness_img))

def saveDarknessLabel(name):
    shutil.copyfile(name + ".txt", name + "_darkness.txt")
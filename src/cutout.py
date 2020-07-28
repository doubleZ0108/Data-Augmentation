import numpy as np
import cv2
from PIL import Image
import shutil

'''
_cutout
    随机抠除四个位置
    用黑色/彩色矩形填充

    Randomly pick out four positions
    Fill with black/color rectangles
'''
def cutout(img):
    min_size_ratio, max_size_ratio = 0.1, 0.3
    channel_wise = False
    max_crop = 4
    replacement=0

    size = np.array(img.shape[:2])
    mini, maxi = min_size_ratio * size, max_size_ratio * size
    cutout_img = img
    for _ in range(max_crop):
        # random size
        h = np.random.randint(mini[0], maxi[0])
        w = np.random.randint(mini[1], maxi[1])
        # random place
        shift_h = np.random.randint(0, size[0] - h)
        shift_w = np.random.randint(0, size[1] - w)

        if channel_wise:
            c = np.random.randint(0, img.shape[-1])
            cutout_img[shift_h:shift_h+h, shift_w:shift_w+w, c] = replacement
        else:
            cutout_img[shift_h:shift_h+h, shift_w:shift_w+w] = replacement

    return Image.fromarray(np.uint8(cutout_img))

def saveCutoutLabel(name):
    shutil.copyfile(name + ".txt", name + "_cutout.txt")
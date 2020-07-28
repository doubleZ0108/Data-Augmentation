import numpy as np
import cv2
from PIL import Image
import shutil

'''
_vignetting
    渐晕
    Image vignetting
'''
def vignetting(img):
    ratio_min_dist=0.2
    range_vignette=np.array((0.2, 0.8))
    random_sign=False

    h, w = img.shape[:2]
    min_dist = np.array([h, w]) / 2 * np.random.random() * ratio_min_dist

    # create matrix of distance from the center on the two axis
    x, y = np.meshgrid(np.linspace(-w/2, w/2, w), np.linspace(-h/2, h/2, h))
    x, y = np.abs(x), np.abs(y)

    # create the vignette mask on the two axis
    x = (x - min_dist[0]) / (np.max(x) - min_dist[0])
    x = np.clip(x, 0, 1)
    y = (y - min_dist[1]) / (np.max(y) - min_dist[1])
    y = np.clip(y, 0, 1)

    # then get a random intensity of the vignette
    vignette = (x + y) / 2 * np.random.uniform(*range_vignette)
    vignette = np.tile(vignette[..., None], [1, 1, 3])

    sign = 2 * (np.random.random() < 0.5) * (random_sign) - 1
    vignetting_img = img * (1 + sign * vignette)

    return Image.fromarray(np.uint8(vignetting_img))

def saveVignettingLabel(name):
    shutil.copyfile(name + ".txt", name + "_vignetting.txt")
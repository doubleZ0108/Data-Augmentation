# coding=utf-8
from PIL import Image
import cv2
import numpy as np

'''
_flip
    图像左右翻转
    Flip the image left and right
'''
def flip(img):
    flip_img = cv2.flip(cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR), 1)
    
    return Image.fromarray(cv2.cvtColor(flip_img,cv2.COLOR_BGR2RGB))

def saveFlipLabel(name):
    with open(name + "_flip.txt", "w") as outfile:
        with open(name + ".txt", "r") as infile:
            for line in infile.readlines():
                words = line.split(" ")
                horizontal_coord = float(words[1])
                outfile.write(words[0] + " " + str(format(1-horizontal_coord, ".6f")) + " " + words[2] + " " + words[3] + " " + words[4])
        
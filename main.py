import cv2 as cv
import numpy as np
from skimage import measure, morphology
from matplotlib import pyplot as plt
from typing import Tuple, List

def get_mask(img):
    img_lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

    l_range = (0, 100)
    ab_range = (-128, 127)

    img_lab = img_lab.astype('int16')
    img_lab[:, :, 0] = img_lab[:, :, 0] * l_range[1] / 255
    img_lab[:, :, 1] += ab_range[0]
    img_lab[:, :, 2] += ab_range[0]

    means = [np.mean(img_lab[:, :, i]) for i in range(3)]
    thresholds = [means[i] - (np.std(img_lab[:, :, i]) / 3) for i in range(3)]
    if sum(means[1:]) <= 0:
        mask = cv.inRange(img_lab, (l_range[0], ab_range[0], ab_range[0]),(thresholds[0], ab_range[1], ab_range[1]))
    else:
        mask = cv.inRange(img_lab, (l_range[0], ab_range[0], ab_range[0]),(thresholds[0], ab_range[1], thresholds[2]))
         

    
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
    cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, mask)
    cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, mask)
    mask = morphology.remove_small_holes(mask, area_threshold=100)
    mask=mask.astype(np.uint8) * 255

    mask=  np.logical_not(mask)
    mask = morphology.remove_small_holes(mask, area_threshold=500)
    mask=  np.logical_not(mask)
    mask=mask.astype(np.uint8) * 255

    return mask


img=cv.imread("/Users/harshitgupta/Downloads/image_shadow_remover/images/test.png")

msk = get_mask(img)


img_lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
kernel = np.ones((5, 5), np.uint8)
dilated = cv.dilate(msk, kernel, iterations=3)
msk1=dilated^msk

total_shadow=0.0
total_border=0.0
num_shadow=0.0
num_border=0.0

r,c,channels=img.shape
new_img=np.zeros((r,c,channels), dtype=np.uint8)

for i in range(r):
    for j in range(c):
        if(msk1[i,j]==255):
            total_border+=img[i][j]
            num_border+=1
        if(msk[i,j]==255):
            total_shadow+=img[i][j]
            num_shadow+=1
            
average_shadow=total_shadow/num_shadow
average_border=total_border/num_border
ratio=1
if(average_shadow[0]!=0 and average_shadow[1]!=0 and average_shadow[2]!=0 ):
    ratio=average_border/average_shadow

for i in range(r):
    for j in range(c):
        if(msk[i,j]==255):
            new_img[i][j]=img[i][j]*ratio
        else:
            new_img[i][j]=img[i][j]

cv.imwrite("output.png",new_img)
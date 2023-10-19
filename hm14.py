import numpy as np
from PIL import Image
import imagehash
from imagehash import phash,whash
import cv2
import glob
import os


l=[]

for img1 in glob.glob("da1/*.png"):
    img1 = cv2.imread(img1)
    img1 = Image.fromarray(img1)
    l.append(phash(img1))


count=0
for i in range(len(l)):
    for j in range(len(l)):
        if i!=j:
            d=l[i]-l[j]
            if d<10:
                count=count+1
print("Duplicate Images:",count)
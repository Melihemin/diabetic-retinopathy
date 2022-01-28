from tqdm import tqdm_notebook as tqdm
import pandas as pd
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np

def processing(files):
    img_list = []

    for i in tqdm(files):
        image = cv2.imread(path + 'train_images\\' + i)
        image = cv2.resize(image, (400,400))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        kopya = image.copy()
        kopya = cv2.cvtColor(kopya, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(kopya, (5,5),0)
        thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)[1]
        kontur = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        kontur = kontur[0][0]
        kontur = kontur[:,0,:]
        x1 = tuple(kontur[kontur[:,0].argmin()])[0]                           
        y1 = tuple(kontur[kontur[:,1].argmin()])[1]
        x2 = tuple(kontur[kontur[:,0].argmax()])[0]
        y2 = tuple(kontur[kontur[:,1].argmax()])[1]
        x = int(x2-x1)*4//50
        y = int(y2-y1)*5//50
        kopya2 = image.copy()                          
        if x2-x1 > 100 and y2-y1 > 100:
            kopya2 = kopya2[y1+y : y2-y, x1+x : x2-x]
            kopya2 = cv2.resize(kopya2,(400,400))
        lab = cv2.cvtColor(kopya2, cv2.COLOR_RGB2LAB)     
        l,a,b  = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=((8,8)))
        cl = clahe.apply(l)
        limg = cv2.merge((cl,a,b))                          
        son = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)
        med_son = cv2.medianBlur(son, 3)
        arka_plan = cv2.medianBlur(son, 37)   
        maske = cv2.addWeighted(med_son, 1, arka_plan, -1, 255)
        son_img = cv2.bitwise_and(maske,med_son)
        img_list.append(son_img)
                                  
    return img_list

    # print(len(img_list))
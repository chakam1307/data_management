import cv2
import numpy as np
import os

DATA_PATH = 'DATA PATH'

def low_resolution(filename, save_filename):
    img = cv2.imread(filename)

    percent = 1
    if(img.shape[1] > img.shape[0]) :      
        percent = 300/img.shape[1]
    else :
        percent = 300/img.shape[0]

    img = cv2.resize(img, dsize=(0, 0), fx=percent, fy=percent, interpolation=cv2.INTER_LINEAR)

    y,x,h,w = (0,0,img.shape[0], img.shape[1])

    w_x = (300-(w-x))/2  
    h_y = (300-(h-y))/2

    if(w_x < 0):    
        w_x = 0
    elif(h_y < 0):
        h_y = 0

    M = np.float32([[1,0,w_x], [0,1,h_y]]) 
    img_re = cv2.warpAffine(img, M, (300, 300))

    cv2.imwrite(save_filename, img_re)

for (path, dir, files) in os.walk(DATA_PATH):
    for file in files:
        file_name = "{}/{}".format(path,file)
        save_filename = "{}/{}/{}".format(path, 'dr' ,file)
        low_resolution(file_name, save_filename)
        print(file_name)



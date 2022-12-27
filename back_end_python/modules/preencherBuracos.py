import cv2 as cv
import numpy as np
import asyncio

async def preencherBuracos(img_or):
    b,g,r = cv.split(img_or)
    contours, hierarchy = cv.findContours(r, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) 
    img = np.zeros([np.shape(r)[0], np.shape(r)[1]], np.uint8)
    img = cv.merge((img,img,img))

    for i in range(len(contours)):
        points=[[np.int(contours[i][j][0][0]),np.int(contours[i][j][0][1])] for j in range(len(contours[i]))]
        cv.fillPoly(img, np.array([points]),(0, 0, 255))
    #fileName = f'./output/{image_name}_preenchido.png'
    #cv.imwrite(fileName, img)
    return img
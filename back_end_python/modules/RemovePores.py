from skimage import morphology
import cv2 as cv
import sys
import asyncio

a = sys.path.append('../modules/')

import fitRemovedPores

async def RemovePores(img_or, poroArea, image_name):
    image_remove = morphology.remove_small_objects(img_or > 2.0, poroArea)
    image_remove = image_remove.astype(int)
    final_image = fitRemovedPores.fitRemovedPores(image_remove)

    fileName = f'./output/{image_name}_preenchido.png'

    cv.imwrite(fileName, final_image)

    return fileName
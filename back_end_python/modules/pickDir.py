import cv2 as cv
import sys
import asyncio
import os

a = sys.path.append('../modules/')

import testPreparedImage

async def pickDir(dirName):
    file_names = os.listdir(dirName)

    for fig in file_names:
        input_image = dirName + '/' + fig
        await testPreparedImage.testImage(input_image)


import cv2 as cv
import sys
import asyncio

a = sys.path.append('../modules/')

import RemovePores, preencherBuracos

async def testImage():

    fileName = '/home/romulo/projetos_pessoais/page_cbpf_/back_end_python/input/4266_PP_5X_SEG_LABEL.png'

    img = cv.imread(fileName)
    
    fileNameBuracos = await preencherBuracos.preencherBuracos(img, fileName[-24:])

    img_preench = cv.imread(fileNameBuracos)

    img_buraco = await RemovePores.RemovePores(img_preench, 300)
    
    cv.imwrite(f'./results/{fileName[-24:]}_test.png', img_buraco)


asyncio.run(testImage())

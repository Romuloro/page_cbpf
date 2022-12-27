import cv2 as cv
import sys
import asyncio

a = sys.path.append('../modules/')

import RemovePores, preencherBuracos

async def testImage(fileName):

    #fileName = '/home/romulo/projetos_pessoais/page_cbpf_/back_end_python/input/4266_PP_5X_SEG_LABEL.png'

    img = cv.imread(fileName)


    fileNamePree = await RemovePores.RemovePores(img, 300, fileName[-24:-4])

    img_preench = cv.imread(fileNamePree)
    
    imgBuracos = await preencherBuracos.preencherBuracos(img_preench)
    
    cv.imwrite(f'./results/{fileName[-24:-4]}_test.png', imgBuracos)


#asyncio.run(testImage())

from skimage import morphology
import sys
import asyncio

a = sys.path.append('../modules/')

import fitRemovedPores

async def RemovePores(img_or, poroArea):
    image_remove = morphology.remove_small_objects(img_or > 2.0, poroArea)
    image_remove = image_remove.astype(int)
    final_image = fitRemovedPores.fitRemovedPores(image_remove)

    return final_image
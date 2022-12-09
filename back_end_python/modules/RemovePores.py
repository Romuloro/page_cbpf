from skimage import morphology
from modules import fitRemovedPores

def RemovePores(img_or, poroArea):
    image_remove = morphology.remove_small_objects(img_or > 2.0, poroArea)
    image_remove = image_remove.astype(int)
    final_image = fitRemovedPores(image_remove)

    return final_image
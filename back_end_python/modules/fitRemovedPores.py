def fitRemovedPores(image_remove):
    for i in range(image_remove.shape[0]):
        for j in range(image_remove.shape[1]):
            if image_remove[i,j][2] == 1:
                image_remove[i,j][2] = 255
    
    return image_remove
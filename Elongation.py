import numpy as np
import cv2 as cv



def elongation(mask):
    #[contours, hierarchy, offset] = cv.findContours(image,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    # cv2.connectedComponentsWithStats(image, connectivity=4,ltype=4)
    #return cv.boundingRect(image)
    #print(image.depth())
    cnts = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
         x, y, w, h = cv.boundingRect(c)
         cv.rectangle(mask, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #cv2.imshow('image', image)
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]

    # print("ligne min, ligne max, colonne min, colonne max : ", rmin, rmax, cmin, cmax)
    # print("hauteur boite : ", rmax-rmin)
    # print("longueur boite : ", cmax-cmin)
    # print("elongation : ", (cmax-cmin)/(rmax-rmin))
    return (cmax-cmin)/(rmax-rmin)

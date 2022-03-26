"""
Extraction des masques des mains
Notre but est de segmenter les masques des mains, par un leurs couleurs.
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import glob

def FillHole(mask):
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    len_contour = len(contours)
    contour_list = []
    for i in range(len_contour):
        drawing = np.zeros_like(mask, np.uint8)  # create a black image
        img_contour = cv.drawContours(drawing, contours, i, (255, 255, 255), -1)
        contour_list.append(img_contour)

    out = sum(contour_list)
    return out

# paramètres:
espace = 'HSV'
nbr_classes = 180
seuil_min = 90
seuil_max = 225

for img in glob.glob('BDD/*.bmp'):
    # lire et affichage de l'image qu'on veut
    image = cv.imread(img)
    print(img)
    chemain = img[4:]
        
    # lire et affichage de l'image qu'on veut
    # image_name = 'boeuf2_1'
    # chemain = "BDD/" + image_name + ".bmp"
    # image = cv.imread(chemain)
    # print(chemain)
    
    
    # redimensionnement de l'image
    dimensions = image.shape
    width = dimensions[0]
    height = dimensions[1]
    image = image[100:int(width * 9 / 10), 100: int(height * 9 / 10)] # extraire une fenetre de l'image
    image = cv.resize(image, (int(width / 2), int(height / 2)))
    # affichage de l'image
   # cv.imshow(image_name, image)
    
    # changement de l'espace colorimetrique
    image_changed = cv.cvtColor(image, eval("cv.COLOR_BGR2" + espace))
    #cv.imshow("image in HSV", image_changed)
    
    (h, s, v) = cv.split(image_changed)
    v[:] = seuil_min
    img = cv.merge((v,v,s))
    rgb = cv.cvtColor(img, cv.COLOR_HSV2RGB)
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    kernel = np.ones((5,5),np.float32)/25
    gray = cv.filter2D(gray,-1,kernel)
    mask = cv.dilate(cv.erode(gray, None, iterations = 3), None, iterations = 3)
    #cv.imshow("gray", gray)
    _, mask = cv.threshold(gray, seuil_min, seuil_max, cv.THRESH_BINARY)
    mask = FillHole(mask)
    
    
    #cv.imshow("image gray", mask)
    
    
    
    
    mat = cv.bitwise_and(image,image, mask = mask)
   # cv.imshow("image in mask", mat)
    # floutage gaussien 
    mat = cv.GaussianBlur(mat, (3, 3), 0)
    
    # grad calculation
    gradx = cv.Sobel(mat,cv.CV_8U,1,0,ksize=3)
    grady=  cv.Sobel(mat,cv.CV_8U,0,1,ksize=3)
    # cv.imshow("gradient de l'image en x", gradx)
    # cv.imshow("gradient de l'image en y", grady)
    grad = cv.add(gradx,grady)
    cv.imshow("gradient total "+chemain, grad) 
    
    #HOG descriptor.
    # hog = cv.HOGDescriptor(grad)
    # h = hog.compute(mat)
    
    
cv.waitKey(0)
cv.destroyWindow()
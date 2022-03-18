import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import glob

def FillHole(mask):
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    len_contour = len(contours)
    contour_list = []
    for i in range(len_contour):
        black_image = np.zeros_like(mask, np.uint8)  # create a black image
        img_contour = cv.drawContours(black_image, contours, i, (255, 255, 255), -1)
        contour_list.append(img_contour)
    out = sum(contour_list)
    return out

# paramètres:
espace = 'HSV'
nbr_classes = 180
seuil_min = 75
seuil_max = 225


for img in glob.glob('BDD/*.bmp'):
    # lire et affichage de l'image qu'on veut
    image = cv.imread(img)
    print(img)
    chemin = img[4:]

    # redimensionnement de l'image
    dimensions = image.shape
    width = dimensions[0]
    height = dimensions[1]
    image = image[100:int(width * 9 / 10), 100: int(height * 9 / 10)] # extraire une fenetre de l'image
    image = cv.resize(image, (int(width / 2), int(height / 2)))
    # affichage de l'image
    # cv.imshow(img, image)

    # changement de l'espace colorimetrique
    image_changed = cv.cvtColor(image, eval("cv.COLOR_BGR2" + espace))
    (h, s, v) = cv.split(image_changed)
    v[:] = 75
    h[:] = int(75 / 2)
    img = cv.merge((v, v, s))
    rgb = cv.cvtColor(img, cv.COLOR_HSV2RGB)
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    # construire le masque
    mask = cv.dilate(cv.erode(gray, None, iterations=3), None, iterations=3)
    _, mask = cv.threshold(gray, seuil_min, seuil_max, cv.THRESH_BINARY)
    mask = FillHole(mask)
    # es = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
    # mask = cv.erode(mask, es, iterations = 1)
    # mask = cv.dilate(mask, es, iterations = 1)


    # cv.imshow("image gray", mask)
    #save images
    chemin_save = "Masques/masque_" + chemin
    status = cv.imwrite(chemin_save, mask)

    print("it's ok")

    if cv.waitKey() & 0xFF == ord('q'):
        break
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import glob

# paramètres:
espace = 'HSV'
nbr_classes = 180
seuil_min = 40
seuil_max = 225
composante_couleur = 1

for img in glob.glob('BDD/*.bmp'):
    # lire et affichage de l'image qu'on veut
    image = cv.imread(img)
    print(img)

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
    # cv.imshow("image in HSV", image_changed)
    # calcul et affichage de l'histogramme de la composante H de l'image (en HSV)
    histogramme = cv.calcHist([image_changed], [composante_couleur], None, [nbr_classes], [0, 180])
    cv.normalize(histogramme, histogramme, 0, 255, cv.NORM_MINMAX)
    plt.plot(histogramme)
    plt.title("histogramme de la composante H (dans HSV) de l'image:  " + img)
    plt.show(block = False)
    plt.pause(0.01)
    plt.clf()

    # construire le masque
    mask = cv.calcBackProject([image_changed], [composante_couleur], histogramme, [0, nbr_classes], 1)
    _, mask2 = cv.threshold(mask, seuil_min, seuil_max, cv.THRESH_BINARY)
    mask2 = cv.erode(cv.dilate(mask, None, iterations = 4), None, iterations = 4)
    _, mask_final = cv.threshold(mask2, 120, 140, cv.THRESH_BINARY)
    # cv.imshow("masque de l'image " + img ,mask_final)
    # save images
    chemain_save = 'Masques/masque_' + img[4:]
    status = cv.imwrite(chemain_save, mask_final)

    print("it's ok")

    if cv.waitKey() & 0xFF == ord('q'):
        break
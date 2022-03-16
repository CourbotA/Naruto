import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import cv2 as cv
import glob

k = 4
ESPACE = "LAB" #YCrCb, HSV, RGB
CH = [0, 2]

index = 0
for image in glob.glob('BDD/*.bmp'):
    index += 1
    print("Image " + str(index) + " : ", image)
    # Lecture et affichage de l'image
    img = cv.imread(image)
    dimensions = img.shape
    width = dimensions[0]
    height = dimensions[1]

    # choisir une fenetre d'ineteret
    img = img[100:int(width * 9 / 10), 100: int(height * 9 / 10)]

    # redimensionner l'image
    img = cv.resize(img, (int(width / 2), int(height / 2)))
    cv.imshow("image " + str(index), img)

    # supprission partielle du fond par buttom hat sur les composantes RGB
    # construire l'élément structurant
    es_size = (3, 3)
    es = cv.getStructuringElement(cv.MORPH_RECT, es_size)

    cv.imshow("iiiiimage test 1 " + str(index), img[:, :, 0])
    cv.imshow("iiiiimage test 2" + str(index), img[:, :, 1])
    cv.imshow("iiiiimage test 3" + str(index), img[:, :, 2])

    for j in range(3):
        img[:, :, j] = cv.GaussianBlur(img[:, :, j], (5, 5), cv.BORDER_DEFAULT)
        # img|:, :, j] = cv.medianBlur(img[:, :, j], 7)

    cv.imshow("image test apres filtrage gaussienne, channel 1" + str(index), img[:, :, 0])
    cv.imshow("image test apres filtrage gaussienne, channel 2" + str(index), img[:, :, 1])
    cv.imshow("image test apres filtrage gaussienne, channel 3" + str(index), img[:, :, 2])

    # filtrage gaussienne pour lissage de l'image
    # img = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)

    # supprimer la moyenne par la FFT
    #Tr_fourier = np.fft.fft2(img)
    #Tr_fourier_shift = np.fftshift(img)
    #img = np.ifft2(Tr_fourier_shift)
    #cv.imshow("image apres suppression de la moyenne" + str(index), img)


    # appliquer un filtre median
    # img = cv.medianBlur(img, 7)

    # Changement d'espace colorimétrique
    img_changed = cv.cvtColor(img, eval("cv.COLOR_BGR2" + ESPACE))
    img_changed_ch = img[:, :, CH].reshape(img.shape[0] * img.shape[1], len(CH))

    plt.scatter(img_changed_ch[:, 0], img_changed_ch[:, 1], s=3)
    plt.show()

    # Algorithme K moyennes
    k_means = KMeans(n_clusters = k)
    pred = k_means.fit_predict(img_changed_ch)

    plt.scatter(img_changed_ch[:, 0], img_changed_ch[:, 1], c=pred, s=3)
    plt.scatter(k_means.cluster_centers_[:, 0], k_means.cluster_centers_[:, 1], s=50, c='red')
    plt.show()

    # Affichage du résultat
    result = pred.reshape(img.shape[0], img.shape[1])
    result = result / (k - 1)

    cv.imshow("kmeans" + str(index), result)

    if cv.waitKey() & 0xFF == ord('q'):
        break


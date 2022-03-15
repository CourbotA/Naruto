import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import cv2 as cv
import glob

k = 2
ESPACE = "LAB"
CH = [0, 2]


for image in glob.glob('BDD/*.bmp'):
    print("Image:", image)
    # Lecture et affichage de l'image
    img = cv.imread(image)
    #dimensions = img.shape
    # img = cv.resize(img, (dimensions[0] / 4, dimensions[1] / 4))
    img = cv.resize(img, (550, 550))
    cv.imshow("image", img)

    # Changement d'espace colorimétrique
    img_changed = cv.cvtColor(img, eval("cv.COLOR_BGR2" + ESPACE))
    img_changed_ch = img[:, :, CH].reshape(img.shape[0] * img.shape[1], len(CH))

    if len(CH) == 2:
        plt.scatter(img_changed_ch[:,0], img_changed_ch[:,1], s = 3)
        plt.show()

    # Algorithme K moyennes
    k_means = KMeans(n_clusters = k)
    pred = k_means.fit_predict(img_changed_ch)

    if len(CH) == 2:
        plt.scatter(img_changed_ch[:, 0], img_changed_ch[:, 1], c = pred, s = 3)
        plt.scatter(k_means.cluster_centers_[:, 0], k_means.cluster_centers_[:, 1], s = 50, c = 'red')
        plt.show()

    # Affichage du résultat
    result = pred.reshape(img.shape[0], img.shape[1])
    result = result / (k - 1)
    cv.imshow("kmeans", result)

    if cv.waitKey() & 0xFF == ord('q'):
        break


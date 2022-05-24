"""
Extraction des masques des mains
Notre but est de segmenter les masques des mains, par un leurs couleurs.
"""


import cv2
import numpy as np
import cv2 as cv

from matplotlib import pyplot as plt
from numpy import linalg as la


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

def hog(img):
    gx = cv.Sobel(img, cv.CV_32F, 1, 0)
    gy = cv.Sobel(img, cv.CV_32F, 0, 1)
    mag, ang = cv.cartToPolar(gx, gy)

    bin_n = 16 # Nombre de bins
    bin = np.int32(bin_n * ang / (2 * np.pi))

    bin_cells, mag_cells = [], []
    cellx = celly = 8

    for i in range(0, int(img.shape[0] / celly)):
        for j in range(0, int(img.shape[1] / cellx)):
            bin_cells.append(bin[i * celly : (i + 1) * celly, j * cellx : (j + 1) * cellx])
            mag_cells.append(mag[i * celly : (i + 1) * celly, j*cellx : (j + 1) * cellx])

    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)

    # transform to Hellinger kernel
    eps = 1e-7
    hist /= hist.sum() + eps #  + eps pour eviter de diviser par 0
    hist = np.sqrt(hist)
    hist /= la.norm(hist) + eps
    # affichage de l'histogramme:
    plt.figure(figsize=(12, 10))
    plt.hist(hist)
    plt.title("l'histogram of HOG")
    plt.show()
    return hist

def count_objects(img):
    #[contours, hierarchy, offset] = cv.findContours(image,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    # cv2.connectedComponentsWithStats(image, connectivity=4,ltype=4)
    #return cv.boundingRect(image)
    #print(image.depth())
    cnts = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
         x, y, w, h = cv2.boundingRect(c)
         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #cv2.imshow('image', image)
    rows = np.any(img, axis=1)
    cols = np.any(img, axis=0)
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]

    print("ligne min, ligne max, colonne min, colonne max : ", rmin, rmax, cmin, cmax)
    print("hauteur boite : ", rmax-rmin)
    print("longueur boite : ", cmax-cmin)
    print("elongation : ", (cmax-cmin)/(rmax-rmin))

    #print("img = ", type(image))
# paramètres:
espace = 'HSV'
nbr_classes = 180
seuil_min = 90
seuil_max = 225

# lire et affichage de l'image qu'on veut
image_name = 'dragon2_3'
chemin = "BDD/" + image_name + ".bmp"
image = cv.imread(chemin)
print(chemin)

# redimensionnement de l'image
dimensions = image.shape
width = dimensions[0]
height = dimensions[1]
image = image[100:int(width * 9 / 10), 100: int(height * 9 / 10)] # extraire une fenetre de l'image
image = cv.resize(image, (int(width / 2), int(height / 2)))
# affichage de l'image
#cv.imshow(image_name, image)

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

nb_components, output, stats, centroids = cv.connectedComponentsWithStats(mask, connectivity=8)

sizes = stats[1:, -1]
nb_components = nb_components - 1

# minimum size to keep an elemen
min_size = np.sum(mask > 0) * 0.5

# answer image as a np.array
mask2 = np.zeros((output.shape))

# for every component in the image, keep it only if it's above min_size
for i in range(0, nb_components):
     if sizes[i] >= min_size:
            mask2[output == i + 1] = 255

mask = mask2.astype(np.uint8)

mask = FillHole(mask)
cv.imshow("image gray", mask)

mat = cv.bitwise_and(image,image, mask = mask)
#cv.imshow("image in mask", mat)

mat = cv.GaussianBlur(mat, (3, 3), 0)

#hog(mat)
count_objects(mask)
cv.imshow("image gray 2", mask)




# grad calculation
gradx = cv.Sobel(mat, cv.CV_8U, 1, 0, ksize=3)
grady = cv.Sobel(mat, cv.CV_8U, 0, 1, ksize=3)

gradX = cv.convertScaleAbs(gradx)
gradY = cv.convertScaleAbs(grady)

grad = cv.addWeighted(gradX, 1, gradY, 1, 0)

#grad = cv2.cvtColor(grad, cv2.COLOR_BGR2GRAY)
_,grad = cv.threshold(grad, 90, 255, cv2.THRESH_BINARY)

#cv.imshow("gradient de l'image en x", gradx)
#cv.imshow("gradient de l'image en y", grady)
cv.imshow("gradient de l'image", grad)

hog = cv.HOGDescriptor("hog.xml");

winStride = (8,8)
padding = (8,8)
locations = ((10,20),)
hog_features = hog.compute(image,winStride,padding,locations)

nb_zones = int(len(hog_features)/9)
hog_max = np.zeros(nb_zones)
freq_HoG = np.zeros(8)
for i in range(0,nb_zones):
    tab_tempo =  hog_features[i*9:i*9+8]
    hog_max[i] = np.argmax(tab_tempo)
for i in range(0,8):
    freq_HoG[i] = np.count_nonzero(hog_max == i)
plt.hist(hog_max)
plt.show()

print("it's ok")

cv.waitKey(0)
#cv.destroyWindow()

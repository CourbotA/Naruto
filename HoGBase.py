import numpy as np
from numpy.linalg import norm
import cv2 as cv
from matplotlib import pyplot as plt
import glob

def hog(image):
    cell_size = (16, 16)  # h x w in pixels
    block_size = (2, 2)  # h x w in cells
    nbins = 9  # number of orientation bins

    # winSize is the size of the image cropped to an multiple of the cell size
    # cell_size is the size of the cells of the img patch over which to calculate the histograms
    # block_size is the number of cells which fit in the patch
    hog = cv.HOGDescriptor(_winSize=(image.shape[1] // cell_size[1] * cell_size[1],
                                      image.shape[0] // cell_size[0] * cell_size[0]),
                            _blockSize=(block_size[1] * cell_size[1],
                                        block_size[0] * cell_size[0]),
                            _blockStride=(cell_size[1], cell_size[0]),
                            _cellSize=(cell_size[1], cell_size[0]),
                            _nbins=nbins)

    hog_features = hog.compute(image)

    nb_zones = int(len(hog_features) / 9)
    hog_max = np.zeros(nb_zones)
    freq_HoG = np.zeros(8)
    for i in range(0, nb_zones):
        tab_tempo = hog_features[i * 9:i * 9 + 8]
        hog_max[i] = np.argmax(tab_tempo)
    for i in range(0, 8):
        freq_HoG[i] = np.count_nonzero(hog_max == i)
    return freq_HoG

i =0
tab_hog = np.zeros((156,8))

for img in glob.glob('ROI/*.bmp'):
    # lire et affichage de l'image qu'on veut
    image = cv.imread(img)
    print(img)
    chemain = img[4:]

    tab_hog[i] = hog(image)
    i+=1

meansclasses = np.zeros((12,8))
varclasses = np.zeros((12,8))
for i in range(0,12):
    meansclasses[i]=np.mean(tab_hog[i:i+12], axis = 0)
    varclasses[i] = np.var(tab_hog[i:i + 12], axis=0)

result = np.zeros(156)
for i in range(0,12):
    for j in range(0,13):
        norms = np.zeros(12)
        for k in range(0, 12):
            norms[k] = norm(tab_hog[i*13+j][1:7]-meansclasses[k][1:7])
        minNorm = np.argmin(norms)
        result[i*13+j] = (minNorm == i)

plt.hist(result)
plt.show()

print("done")

cv.waitKey(0)








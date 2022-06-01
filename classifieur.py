#Supposition répartition gaussienne des classes.
import glob
import scipy.stats
import Elongation
from handDetect import HandsLandmarks, HandsLandmarksSingleIm
from Squeletization import Squeletizer
from Masque import Masquecalculator
import cv2 as cv
import numpy as np
from sklearn.naive_bayes import GaussianNB

def apprentissage():
    taille = 9
    tab_ref = ["chien", "boeuf", "cheval", "chevre", "cochon", "dragon", "lapin", "oiseau", "rat", "serpent", "singe",
               "tigre"]
    att1 = []
    att2 = []
    att3 = []

    for imgpath in glob.glob('Apprentissage/*.bmp'):
        # lire et affichage de l'image qu'on veut
        maskclass = Masquecalculator(imgpath)
        img = maskclass.resize_image()
        masque = maskclass.mask()

        Roi = img.copy()
        Roi[:,:,2] = np.multiply(masque, img[:,:,0])
        Roi[:,:,1] = np.multiply(masque, img[:,:,1])
        Roi[:,:,0] = np.multiply(masque, img[:,:,2])

        squele = Squeletizer()
        att1.append(Elongation.elongation(masque))
        att2.append(squele.calculate(Roi,masque))
        att3.append(HandsLandmarksSingleIm(imgpath))
    model_Gaussian = GaussianNB()
    Xtrain = np.zeros((12*taille,59))

    for i in range(12*taille):
        print(att3[i])
        Xtrain[i,:] = [att1[i]]+att2[i]+att3[i]
    Ytrain = ["chien"]*9 + ["boeuf"]*9 + ["cheval"]*9 + ["chevre"]*9 + ["cochon"]*9 + ["dragon"]*9 + ["lapin"]*9 + ["oiseau"]*9 + ["rat"]*9 + ["serpent"]*9 + ["singe"]*9 + ["tigre"]*9
    model_Gaussian.fit(Xtrain,Ytrain)

    att1_test = []
    att2_test = []
    att3_test = []

    for imgpath in glob.glob('Test/*.bmp'):
        maskclass = Masquecalculator(imgpath)
        img = maskclass.resize_image()
        masque = maskclass.mask()

        Roi = img.copy()
        Roi[:, :, 2] = np.multiply(masque, img[:, :, 0])
        Roi[:, :, 1] = np.multiply(masque, img[:, :, 1])
        Roi[:, :, 0] = np.multiply(masque, img[:, :, 2])

        squele = Squeletizer()
        att1_test.append(Elongation.elongation(masque))
        att2_test.append(squele.calculate(Roi, masque))
        att3_test.append(HandsLandmarksSingleIm(imgpath)) #à mettre la bonne fonction
    Xtest = np.zeros((12*(13-taille),59))
    for i in range(12*(13-taille)):
        Xtest[i,:] = [att1_test[i]]+att2_test[i]+att3_test[i][0,:]+att3_test[i][1,:]
    prediction = model_Gaussian.predict(Xtest)

    verite = ["chien"]*4 + ["boeuf"]*4 + ["cheval"]*4 + ["chevre"]*4 + ["cochon"]*4 + ["dragon"]*4 + ["lapin"]*4 + ["oiseau"]*4 + ["rat"]*4 + ["serpent"]*4 + ["singe"]*4 + ["tigre"]*4

    score = model_Gaussian.score(Xtest,verite)
    print(score)
apprentissage()

#Supposition répartition gaussienne des classes.
import glob
import scipy.stats
import Elongation
from handDetect import HandsLandmarksSingleIm, HandsLandmarksProd
from Squeletization import Squeletizer
from Masque import Masquecalculator
import cv2 as cv
import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier



class ClassifierP:
    def build(self):
        taille = 13
        tab_ref = ["chien", "boeuf", "cheval", "chevre", "cochon", "dragon", "lapin", "oiseau", "rat", "serpent", "singe",
                   "tigre"]
        att1 = []
        att2 = []
        att3 = []
        for imgpath in glob.glob('Apprentissage/*.bmp'):
            # lire et affichage de l'image qu'on veut
            self.maskclass = Masquecalculator(imgpath)
            img = self.maskclass.resize_image()
            masque = self.maskclass.mask()

            Roi = img.copy()
            Roi[:,:,2] = np.multiply(masque, img[:,:,0])
            Roi[:,:,1] = np.multiply(masque, img[:,:,1])
            Roi[:,:,0] = np.multiply(masque, img[:,:,2])

            self.squele = Squeletizer()
            att1.append(Elongation.elongation(masque))
            att2.append(self.squele.calculate(Roi,masque))
            att3.append(HandsLandmarksSingleIm(imgpath))
        self.model_histGrad = HistGradientBoostingClassifier()
        Xtrain = np.zeros((12*taille,59))
        for i in range(12*taille):
            Xtrain[i,:] = [att1[i]]+att2[i]+att3[i]
        Ytrain = ["chien"]*13 + ["boeuf"]*13 + ["cheval"]*13 + ["chevre"]*13 + ["cochon"]*13 + ["dragon"]*13 + ["lapin"]*13 + ["oiseau"]*13 + ["rat"]*13 + ["serpent"]*13 + ["singe"]*13 + ["tigre"]*13
        self.model_histGrad.fit(Xtrain,Ytrain)

    def classify(self,image):
        self.maskclass.set_image_raw(image)
        img = self.maskclass.resize_image()
        masque = self.maskclass.mask()

        Roi = img.copy()
        Roi[:, :, 2] = np.multiply(masque, img[:, :, 0])
        Roi[:, :, 1] = np.multiply(masque, img[:, :, 1])
        Roi[:, :, 0] = np.multiply(masque, img[:, :, 2])

        el = Elongation.elongation(masque)
        squel = self.squele.calculate(Roi, masque)
        media = HandsLandmarksProd(img)
        X = np.zeros(59)
        X = [el] + squel +media

        prediction = self.model_histGrad.predict(X)

        return prediction[0]



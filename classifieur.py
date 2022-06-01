#Supposition répartition gaussienne des classes.
import glob
import scipy.stats
from Masque2 import count_objects
from handDetect import HandsLandmarks
import TestSquel
import cv2 as cv
import numpy as np
from sklearn.naive_bayes import GaussianNB

class Signe:
    def __init__(self,classname):
        self.classname = classname
        self.moy = None
        self.std = None

    def get_Classname(self):
        return self.classname

    def get_Moy(self):
        return self.moy

    def get_Std(self):
        return self.std

    def set_Classname(self,name):
        self.classname = name

    def set_Moy(self, moy):
        self.moy = moy

    def set_Std(self, std):
        self.std = std

tab_signes = []


def apprentissage():
    taille = 9
    tab_ref = ["chien", "boeuf", "cheval", "chevre", "cochon", "dragon", "lapin", "oiseau", "rat", "serpent", "singe",
               "tigre"]
    att1 = []
    att2 = []
    att3 = []
    for img in glob.glob('BDD/apprentissage/*.bmp'):
        # lire et affichage de l'image qu'on veut
        #image = cv.imread(img)
        att1.append(count_objects(img))
        att2.append(TestSquel.area_opening(img))  #à mettre la bonne fonction
        att3.append(HandsLandmarks()) #à mettre la bonne fonction
    model_Gaussian = GaussianNB()
    Xtrain = np.zeros((12*taille,59))
    for i in range(12*taille):
        Xtrain[i,:] = [att1[i]]+att2[i]+att3[i][0,:]+att3[i][1,:]
    Ytrain = ["chien"]*9 + ["boeuf"]*9 + ["cheval"]*9 + ["chevre"]*9 + ["cochon"]*9 + ["dragon"]*9 + ["lapin"]*9 + ["oiseau"]*9 + ["rat"]*9 + ["serpent"]*9 + ["singe"]*9 + ["tigre"]*9
    model_Gaussian.fit(Xtrain,Ytrain)
    att1_test = []
    att2_test = []
    att3_test = []
    for img in glob.glob('BDD/test/*.bmp'):
        # lire et affichage de l'image qu'on veut
        #image = cv.imread(img)
        att1.append(count_objects(img))
        att2.append(TestSquel.area_opening(img))  #à mettre la bonne fonction
        att3.append(HandsLandmarks()) #à mettre la bonne fonction
    Xtest = np.zeros((12*taille,59))
    for i in range(12*taille):
        Xtest[i,:] = [att1_test[i]]+att2_test[i]+att3_test[i][0,:]+att3_test[i][1,:]
    prediction = model_Gaussian.predict(Xtest)
    print(prediction)
    # y_te
    # precision = accuracy_score(y_test, prediction) * 100
    # for i in range(12):
    #     vals1 = att1[i*taille+0:(i+1)*taille - 1]   #élongation
    #     vals2 = att2[i*taille+0:(i+1)*taille - 1]   #squelette bizarre gradient de clément
    #     vals3 = att3[i*taille+0:(i+1)*taille - 1]   #données de la librairie google
    #
    #     #traitement des tableaux d'attributs pour calculer une moyenne/cov. Pas besoin pour vals1.
    #     std = []
    #     moy = []
    #
    #     vals1 = np.array(vals1)
    #     vals2 = np.array(vals2)
    #     vals3 = np.array(vals3)
    #
    #     #vals1
    #     moy.append(np.sum(vals1)/len(vals1))
    #     std.append(np.std(vals1))
    #
    #     #vals2
    #     elmt_moy = []
    #     elmt_std = []
    #     for l in range(16):
    #         for k in range(0, taille):
    #             elmt_std.append(vals2[k][l])
    #             elmt_moy.append(vals2[k][l])
    #         elmt_std = np.array(elmt_std)
    #         elmt_moy = np.array(elmt_moy)
    #         std.append(np.std(elmt_std))
    #         moy.append(np.sum(elmt_moy)/len(elmt_moy))
    #         elmt_moy = np.setdiff1d(elmt_moy,elmt_moy)
    #         elmt_std = np.setdiff1d(elmt_std,elmt_std)
    #
    #     #vals3  21x2 tab
    #     elmt_moy = []
    #     elmt_std = []
    #     for l in range(21):
    #         for m in range(2):
    #             for k in range(0, taille):
    #                 elmt_std.append(vals3[k][l][m])
    #                 elmt_moy.append(vals3[k][l][m])
    #             elmt_std = np.array(elmt_std)
    #             elmt_moy = np.array(elmt_moy)
    #             std.append(np.std(elmt_std))
    #             moy.append(np.sum(elmt_moy) / len(elmt_moy))
    #             elmt_moy = np.setdiff1d(elmt_moy, elmt_moy)
    #             elmt_std = np.setdiff1d(elmt_std, elmt_std)
    #
    #     #fin du traitement : création du signe correspondant
    #     sig = Signe(tab_ref[i])
    #     sig.set_Moy(moy)
    #     sig.set_Std(std)
    #     tab_signes.append(sig)

def ifzero(tab):
    pos = False
    neg = False
    i=0
    while (not(pos) and not(neg)) or i >= len(tab):
        if tab[i] > 0:
            pos = True
        elif tab[i] < 0:
            neg = True
        else:
            pos = True
            neg = True
        i=i+1
    return (pos != 0 and neg !=0)

def calc_frontiere():
    Papriori = 1/12
    x = np.linspace(-1,30,310)
    gaussienne = np.zeros((12,59))
    frontiere_pts = np.zeros((12,12,59))   #choisir 2 classes parmi les 12 possibles revient à sélectionner une frontière
    for i in range(12): #nb signes
        for j in range(59): #nb gaussiennes par signe = nb sous-caractéristiques par image
            gaussienne[i,j] = np.array(scipy.stats.norm.pdf(x, tab_signes[i].moy[j], tab_signes[i].std[j])*Papriori)
        for class2 in range(12):
            for pt in range(59):
                frontiere_pts[i,class2,pt] = ifzero(gaussienne[i,pt] - gaussienne[class2,pt])
    gaussienne = np.array(gaussienne)
    Paposteriori = gaussienne / sum(gaussienne)


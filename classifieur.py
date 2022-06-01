#Supposition répartition gaussienne des classes.
import glob
import scipy.stats
from Masque2 import count_objects
#import handDetect
import TestSquel
import cv2 as cv
import numpy as np

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
        #att3.append(handDetect.hand_world_landmarks) #à mettre la bonne fonction
    for i in range(12):
        vals1 = att1[i*taille+0:(i+1)*taille - 1]   #élongation
        vals2 = att2[i*taille+0:(i+1)*taille - 1]   #squelette bizarre gradient de clément
        #vals3 = att3[i*taille+0:(i+1)*taille - 1]   #données de la librairie google

        #traitement des tableaux d'attributs pour calculer une moyenne/cov. Pas besoin pour vals1.
        std = []
        moy = []

        vals1 = np.array(vals1)
        vals2 = np.array(vals2)
        #vals3 = np.array(vals3)

        #vals1
        moy.append(np.sum(vals1)/len(vals1))
        std.append(np.std(vals1))

        #vals2
        elmt_moy = []
        elmt_std = []
        for l in range(16):
            for k in range(0, taille):
                elmt_std.append(vals2[k][l])
                elmt_moy.append(vals2[k][l])
            elmt_std = np.array(elmt_std)
            elmt_moy = np.array(elmt_moy)
            std.append(np.std(elmt_std))
            moy.append(np.sum(elmt_moy)/len(elmt_moy))
            elmt_moy = np.setdiff1d(elmt_moy,elmt_moy)
            elmt_std = np.setdiff1d(elmt_std,elmt_std)

        #vals3  21x2 tab

        #fin du traitement : création du signe correspondant
        sig = Signe(tab_ref[i])
        sig.set_Moy(moy)
        sig.set_Std(std)
        tab_signes.append(sig)

def calc_frontiere():
    Papriori = 1/12
    x = np.linspace(-1,30,310)
    gaussienne = []
    for i in range(12):
        for j in range(59):
            gaussienne.append(np.array(scipy.stats.norm.pdf(x, tab_signes[i].moy[j], tab_signes[i].std[j]))*Papriori)
    gaussienne = np.array(gaussienne)
    Paposteriori = gaussienne / sum(gaussienne)

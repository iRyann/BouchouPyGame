import pygame
import time
from constantes import *

class Presentation:
    def __init__(self):
        pygame.init()

        # charger toutes les images du jeu

        self.imgFondEcran = pygame.image.load("images/autres/fondEcran.png")
        self.imgMarioBas10 = pygame.image.load("images/mario/bas10.png")
        self.imgMarioBas10Saut = pygame.image.load("images/mario/bas10_saut.png")
        self.imgMarioBas11 = pygame.image.load("images/mario/bas11.png")
        self.imgMarioBas12 = pygame.image.load("images/mario/bas12.png")
        self.imgMarioBas13 = pygame.image.load("images/mario/bas13.png")
        self.imgMarioBas16Saut = pygame.image.load("images/mario/bas16_saut.png")
        self.imgMarioBas14 = pygame.image.load("images/mario/bas14.png")
        self.imgMarioBas15 = pygame.image.load("images/mario/bas15.png")
        self.imgMarioBas16 = pygame.image.load("images/mario/bas16.png")
        self.imgMarioBas18 = pygame.image.load("images/mario/bas18.png")
        self.imgMarioBas20 = pygame.image.load("images/mario/bas20.png")
        self.imgMarioBas21 = pygame.image.load("images/mario/bas21.png")
        self.imgMarioBas22 = pygame.image.load("images/mario/bas22.png")
        self.imgMarioBas22Saut = pygame.image.load("images/mario/bas22_saut.png")
        self.imgMarioBas23 = pygame.image.load("images/mario/bas23.png")
        self.imgMarioBas23Saut = pygame.image.load("images/mario/bas23_saut.png")
        self.imgMarioBas24 = pygame.image.load("images/mario/bas24.png")
        self.imgMarioBas24Saut = pygame.image.load("images/mario/bas24_saut.png")
        self.imgMarioBas26 = pygame.image.load("images/mario/bas26.png")
        self.imgMarioBas27 = pygame.image.load("images/mario/bas27.png")
        self.imgMarioBas28 = pygame.image.load("images/mario/bas28.png")
        self.imgMarioEchelle0 = pygame.image.load("images/mario/echelle0.png")
        self.imgMarioEchelle1 = pygame.image.load("images/mario/echelle1.png")
        self.imgMarioHaut0 = pygame.image.load("images/mario/haut0.png")
        self.imgMarioHaut0Levier = pygame.image.load("images/mario/haut0_levier.png")
        self.imgMarioHaut1 = pygame.image.load("images/mario/haut1.png")
        self.imgMarioHaut2 = pygame.image.load("images/mario/haut2.png")
        self.imgMarioHautSaut = pygame.image.load("images/mario/haut_saut.png")
        self.imgMarioHautEchec0 = pygame.image.load("images/mario/haut_echec0.png")
        self.imgMarioHautEchec1 = pygame.image.load("images/mario/haut_echec1.png")
        self.imgMarioHautSucces0 = pygame.image.load("images/mario/haut_succes0.png")
        self.imgMarioHautSucces1 = pygame.image.load("images/mario/haut_succes1.png")
        self.imgMarioHautSucces2 = pygame.image.load("images/mario/haut_succes2.png")
        self.imgMarioEchec = pygame.image.load("images/mario/echec.png")

        self.imgTonneauHaut0 = pygame.image.load("images/tonneau/tonneau_haut0.png")
        self.imgTonneauHaut1 = pygame.image.load("images/tonneau/tonneau_haut1.png")
        self.imgTonneauHaut2 = pygame.image.load("images/tonneau/tonneau_haut2.png")
        self.imgTonneauRoule0 = pygame.image.load("images/tonneau/tonneau_roule0.png")
        self.imgTonneauRoule1 = pygame.image.load("images/tonneau/tonneau_roule1.png")
        self.imgTonneauRoule2 = pygame.image.load("images/tonneau/tonneau_roule2.png")
        self.imgTonneauRoule3 = pygame.image.load("images/tonneau/tonneau_roule3.png")
        self.imgTonneauLance = pygame.image.load("images/tonneau/tonneau_lance.png")

        self.imgDK0 = pygame.image.load("images/dk/dk0.png")
        self.imgDK1 = pygame.image.load("images/dk/dk1.png")
        self.imgDK2 = pygame.image.load("images/dk/dk2.png")
        self.imgDK0Tonneau = pygame.image.load("images/dk/dk0_tonneau.png")
        self.imgDK1Tonneau = pygame.image.load("images/dk/dk1_tonneau.png")
        self.imgDK2Tonneau = pygame.image.load("images/dk/dk2_tonneau.png")
        self.imgDKTombe = pygame.image.load("images/dk/dk_tombe.png")

        self.imgCoeur = pygame.image.load("images/autres/coeur.png")

        self.imgBarre0 = pygame.image.load("images/barre/barre0.png")
        self.imgBarre1 = pygame.image.load("images/barre/barre1.png")
        self.imgBarre2 = pygame.image.load("images/barre/barre2.png")
        self.imgBarre3 = pygame.image.load("images/barre/barre3.png")
        self.imgBarre4 = pygame.image.load("images/barre/barre4.png")

        self.imgEchafaudage0 = pygame.image.load("images/echafaudage/echafaudage0.png")
        self.imgEchafaudage1 = pygame.image.load("images/echafaudage/echafaudage1.png")
        self.imgCrochet0 = pygame.image.load("images/echafaudage/crochet0.png")
        self.imgCrochet1 = pygame.image.load("images/echafaudage/crochet1.png")
        self.imgCrochet2 = pygame.image.load("images/echafaudage/crochet2.png")
        self.imgCrochet3 = pygame.image.load("images/echafaudage/crochet3.png")

        self.imgLevier0 = pygame.image.load("images/grue/levier0.png")
        self.imgLevier1 = pygame.image.load("images/grue/levier1.png")
        self.imgGrue0 = pygame.image.load("images/grue/grue0.png")
        self.imgGrue1 = pygame.image.load("images/grue/grue1.png")
        self.imgGrue2 = pygame.image.load("images/grue/grue2.png")
        self.imgGrue3 = pygame.image.load("images/grue/grue3.png")
        self.imgGrue4 = pygame.image.load("images/grue/grue4.png")
        self.imgGrueOff = pygame.image.load("images/grue/grue_off.png")

        self.imgChiffre0 = pygame.image.load("images/chiffres/0.png")
        self.imgChiffre1 = pygame.image.load("images/chiffres/1.png")
        self.imgChiffre2 = pygame.image.load("images/chiffres/2.png")
        self.imgChiffre3 = pygame.image.load("images/chiffres/3.png")
        self.imgChiffre4 = pygame.image.load("images/chiffres/4.png")
        self.imgChiffre5 = pygame.image.load("images/chiffres/5.png")
        self.imgChiffre6 = pygame.image.load("images/chiffres/6.png")
        self.imgChiffre7 = pygame.image.load("images/chiffres/7.png")
        self.imgChiffre8 = pygame.image.load("images/chiffres/8.png")
        self.imgChiffre9 = pygame.image.load("images/chiffres/9.png")

        # créer la fenêtre avec l'image du fond et le titre

        pygame.display.set_caption("Donkey Kong")
        pygame.display.set_icon(pygame.image.load("images/autres/iconeFenetre.png"))
        self.ecran = pygame.display.set_mode((909, 792))
        self.ecran.blit(self.imgFondEcran, (0, 0))

        pygame.display.update()

    # ------------------------------------------------------------------------
    # retourner la touche sur laquelle a appuyé le joueur ou fermer la fenêtre
    # si clic sur la croix

    def lireEvenement(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key in [pygame.K_SPACE, pygame.K_UP, pygame.K_RIGHT,
                                     pygame.K_DOWN, pygame.K_LEFT]:
                    return evenement.key
        return Constantes.AUCUN

    # ------------------------------------------------------------------------
    # fermer la fenêtre si clic sur la croix

    def attendreFermetureFenetre(self):
        while True:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            time.sleep(0.2)

    # ------------------------------------------------------------------------
    # afficher Mario

    def afficherMario(self, ligne, position, etat):
        if ligne == 0:
            if etat == Constantes.NORMAL:
                if position == 0:
                    self.afficherImage(74, 219, self.imgMarioHaut0)
                elif position == 1:
                    self.afficherImage(222, 216, self.imgMarioHaut1)
                elif position == 2:
                    self.afficherImage(308, 216, self.imgMarioHaut2)
            elif etat == Constantes.LEVIER:
                if position == 0:
                    self.afficherImage(74, 219, self.imgMarioHaut0Levier)
            elif etat == Constantes.SAUT:
                self.afficherImage(377, 165, self.imgMarioHautSaut)
        elif ligne == 1:
            self.afficherImage(59, 325, self.imgMarioEchelle0)
        elif ligne == 2:
            self.afficherImage(54, 438, self.imgMarioEchelle1)
        elif ligne == 3:
            if etat == Constantes.NORMAL:
                if position == 0:
                    self.afficherImage(52, 485, self.imgMarioBas28)
                elif position == 1:
                    self.afficherImage(101, 491, self.imgMarioBas27)
                elif position == 2:
                    self.afficherImage(150, 493, self.imgMarioBas26)
                elif position == 3:
                    self.afficherImage(198, 497, self.imgMarioBas21)
                elif position == 4:
                    self.afficherImage(246, 502, self.imgMarioBas24)
                elif position == 5:
                    self.afficherImage(294, 507, self.imgMarioBas23)
                elif position == 6:
                    self.afficherImage(338, 509, self.imgMarioBas22)
                elif position == 7:
                    self.afficherImage(390, 515, self.imgMarioBas21)
                elif position == 8:
                    self.afficherImage(432, 519, self.imgMarioBas20)
            elif etat == Constantes.SAUT:
                if position == 4:
                    self.afficherImage(246, 460, self.imgMarioBas22Saut)
                elif position == 5:
                    self.afficherImage(297, 463, self.imgMarioBas23Saut)
                elif position == 6:
                    self.afficherImage(338, 466, self.imgMarioBas24Saut)
        elif ligne == 4:
            if etat == Constantes.NORMAL:
                if position == 0:
                    self.afficherImage(54, 676, self.imgMarioBas10)
                elif position == 1:
                    self.afficherImage(102, 672, self.imgMarioBas11)
                elif position == 2:
                    self.afficherImage(150, 669, self.imgMarioBas12)
                elif position == 3:
                    self.afficherImage(198, 664, self.imgMarioBas13)
                elif position == 4:
                    self.afficherImage(246, 661, self.imgMarioBas14)
                elif position == 5:
                    self.afficherImage(294, 655, self.imgMarioBas15)
                elif position == 6:
                    self.afficherImage(338, 655, self.imgMarioBas16)
                elif position == 7:
                    self.afficherImage(390, 649, self.imgMarioBas13)
                elif position == 8:
                    self.afficherImage(432, 647, self.imgMarioBas18)
            elif etat == Constantes.SAUT:
                if position == 0:
                    self.afficherImage(54, 641, self.imgMarioBas10Saut)
                elif position == 6:
                    self.afficherImage(338, 615, self.imgMarioBas16Saut)

    # ------------------------------------------------------------------------
    # afficher un tonneau

    def afficherTonneau(self, ligne, position):
        if ligne == 0:
            if position == 0:
                self.afficherImage(108, 127, self.imgTonneauLance)
            elif position == 1:
                self.afficherImage(218, 127, self.imgTonneauLance)
            elif position == 2:
                self.afficherImage(318, 127, self.imgTonneauLance)
        elif ligne == 1:
            if position == 0:
                self.afficherImage(108, 187, self.imgTonneauHaut0)
            elif position == 1:
                self.afficherImage(218, 187, self.imgTonneauHaut1)
            elif position == 2:
                self.afficherImage(318, 187, self.imgTonneauHaut2)
        elif ligne == 2:
            if position == 0:
                self.afficherImage(108, 273, self.imgTonneauHaut0)
            elif position == 1:
                self.afficherImage(218, 273, self.imgTonneauHaut1)
            elif position == 2:
                self.afficherImage(318, 273, self.imgTonneauHaut2)
        elif ligne == 3:
            if position == 0:
                self.afficherImage(3, 348, self.imgTonneauRoule3)
            if position == 1:
                self.afficherImage(55, 339, self.imgTonneauRoule0)
            elif position == 2:
                self.afficherImage(108, 335, self.imgTonneauRoule1)
            elif position == 3:
                self.afficherImage(163, 330, self.imgTonneauRoule2)
            elif position == 4:
                self.afficherImage(218, 326, self.imgTonneauRoule3)
            elif position == 5:
                self.afficherImage(268, 322, self.imgTonneauRoule0)
            elif position == 6:
                self.afficherImage(318, 317, self.imgTonneauRoule1)
        elif ligne == 4:
            if position == 0:
                self.afficherImage(3, 426, self.imgTonneauRoule2)
        elif ligne == 5:
            if position == 0:
                self.afficherImage(3, 495, self.imgTonneauRoule1)
            elif position == 1:
                self.afficherImage(54, 499, self.imgTonneauRoule2)
            elif position == 2:
                self.afficherImage(102, 504, self.imgTonneauRoule3)
            elif position == 3:
                self.afficherImage(150, 507, self.imgTonneauRoule0)
            elif position == 4:
                self.afficherImage(198, 512, self.imgTonneauRoule1)
            elif position == 5:
                self.afficherImage(246, 516, self.imgTonneauRoule2)
            elif position == 6:
                self.afficherImage(294, 521, self.imgTonneauRoule3)
            elif position == 7:
                self.afficherImage(342, 525, self.imgTonneauRoule0)
            elif position == 8:
                self.afficherImage(390, 530, self.imgTonneauRoule1)
            elif position == 9:
                self.afficherImage(438, 533, self.imgTonneauRoule2)
            elif position == 10:
                self.afficherImage(486, 558, self.imgTonneauRoule3)
        elif ligne == 6:
            if position == 0:
                self.afficherImage(3, 694, self.imgTonneauRoule0)
            elif position == 1:
                self.afficherImage(54, 690, self.imgTonneauRoule1)
            elif position == 2:
                self.afficherImage(102, 685, self.imgTonneauRoule2)
            elif position == 3:
                self.afficherImage(150, 682, self.imgTonneauRoule3)
            elif position == 4:
                self.afficherImage(198, 678, self.imgTonneauRoule0)
            elif position == 5:
                self.afficherImage(246, 675, self.imgTonneauRoule1)
            elif position == 6:
                self.afficherImage(294, 670, self.imgTonneauRoule2)
            elif position == 7:
                self.afficherImage(342, 667, self.imgTonneauRoule3)
            elif position == 8:
                self.afficherImage(390, 664, self.imgTonneauRoule0)
            elif position == 9:
                self.afficherImage(438, 661, self.imgTonneauRoule1)
            elif position == 10:
                self.afficherImage(486, 656, self.imgTonneauRoule2)

    # ------------------------------------------------------------------------
    # afficher Donkey Kong

    def afficherDonkeyKong(self, positionDK, etatDK):
        if etatDK == Constantes.NORMAL:
            if positionDK == 0:
                self.afficherImage(79, 19, self.imgDK0)
            elif positionDK == 1:
                self.afficherImage(175, 17, self.imgDK1)
            elif positionDK == 2:
                self.afficherImage(283, 16, self.imgDK2)
        elif etatDK == Constantes.TONNEAU:
            if positionDK == 0:
                self.afficherImage(79, 19, self.imgDK0Tonneau)
            elif positionDK == 1:
                self.afficherImage(175, 17, self.imgDK1Tonneau)
            elif positionDK == 2:
                self.afficherImage(283, 16, self.imgDK2Tonneau)

    # ------------------------------------------------------------------------
    # afficher la barre métallique

    def afficherBarre(self, positionBarre):
        if positionBarre == 0:
            self.afficherImage(26, 397, self.imgBarre0)
        elif positionBarre == 1:
            self.afficherImage(73, 402, self.imgBarre3)
        elif positionBarre == 2:
            self.afficherImage(120, 406, self.imgBarre2)
        elif positionBarre == 3:
            self.afficherImage(167, 410, self.imgBarre1)
        elif positionBarre == 4:
            self.afficherImage(214, 413, self.imgBarre0)
        elif positionBarre == 5:
            self.afficherImage(261, 418, self.imgBarre1)
        elif positionBarre == 6:
            self.afficherImage(308, 422, self.imgBarre2)
        elif positionBarre == 7:
            self.afficherImage(355, 426, self.imgBarre3)
        elif positionBarre == 8:
            self.afficherImage(395, 429, self.imgBarre4)

    # ------------------------------------------------------------------------
    # afficher la grue

    def afficherGrue(self, positionGrue, etatGrue):
        if etatGrue == Constantes.NORMAL:
            if positionGrue == 0:
                self.afficherImage(430, 134, self.imgGrue0)
            elif positionGrue == 1:
                self.afficherImage(430, 134, self.imgGrue1)
            elif positionGrue == 2:
                self.afficherImage(430, 134, self.imgGrue2)
            elif positionGrue == 3:
                self.afficherImage(430, 134, self.imgGrue3)
            elif positionGrue == 4:
                self.afficherImage(430, 134, self.imgGrue4)
        else:
            self.afficherImage(518, 213, self.imgGrueOff)


    # ------------------------------------------------------------------------
    # afficher le levier pour la grue

    def afficherLevier(self, etatGrue):
        if etatGrue == Constantes.NORMAL:
            self.afficherImage(48, 232, self.imgLevier1)
        else:
            self.afficherImage(48, 232, self.imgLevier0)

    # ------------------------------------------------------------------------
    # afficher Mario qui retire un crochet

    def afficherMarioSucces(self, numSequence):
        if numSequence == 1:
            self.afficherImage(455, 29, self.imgMarioHautSucces0)
        elif numSequence == 2:
            self.afficherImage(430, 134, self.imgMarioHautSucces1)
        elif numSequence == 3:
            self.afficherImage(518, 213, self.imgMarioHautSucces2)

    # ------------------------------------------------------------------------
    # afficher Mario qui retire le dernier crochet (l'échafaudage tombe)

    def afficherMarioSuccesDK(self, numSequence):
        if numSequence == 1:
            self.afficherImage(455, 29, self.imgMarioHautSucces0)
        elif numSequence == 2:
            self.afficherImage(455, 29, self.imgMarioHautSucces0)
            self.afficherImage(358, 276, self.imgDKTombe)
        elif numSequence == 3:
            self.afficherImage(455, 29, self.imgMarioHautSucces0)
            self.afficherImage(358, 276, self.imgDKTombe)
            self.afficherImage(40, 3, self.imgCoeur)
        elif numSequence == 4:
            self.afficherImage(430, 134, self.imgMarioHautSucces1)
            self.afficherImage(358, 276, self.imgDKTombe)
        elif numSequence == 5:
            self.afficherImage(518, 213, self.imgMarioHautSucces2)
            self.afficherImage(358, 276, self.imgDKTombe)

    # ------------------------------------------------------------------------
    # Mario a loupé la grue et il tombe

    def afficherMarioEchec(self, numSequence):
        if numSequence == 1:
            self.afficherImage(423, 252, self.imgMarioHautEchec0)
        elif numSequence == 2:
            self.afficherImage(461, 321, self.imgMarioHautEchec1)

    # ------------------------------------------------------------------------
    # afficher l'échafaudage

    def afficherEchafaudage(self, nbCrochets):
        if nbCrochets == 0:
            self.afficherImage(1, 146, self.imgEchafaudage1)
        elif nbCrochets == 1:
            self.afficherImage(401, 63, self.imgCrochet0)
            self.afficherImage(78, 104, self.imgEchafaudage0)
        elif nbCrochets == 2:
            self.afficherImage(401, 63, self.imgCrochet1)
            self.afficherImage(78, 104, self.imgEchafaudage0)
        elif nbCrochets == 3:
            self.afficherImage(401, 63, self.imgCrochet2)
            self.afficherImage(78, 104, self.imgEchafaudage0)
        elif nbCrochets == 4:
            self.afficherImage(401, 63, self.imgCrochet3)
            self.afficherImage(78, 104, self.imgEchafaudage0)

    # ------------------------------------------------------------------------
    # afficher les échecs à droite de l'écran

    def afficherEchecs(self, nbEchecs):
        for i in range(nbEchecs):
            self.afficherImage(683 + (i * 49), 382, self.imgMarioEchec)

    # ------------------------------------------------------------------------
    # afficher le score

    def afficherScore(self, score):
        self.afficherChiffre(658, int(score / 1000))
        self.afficherChiffre(707, int(score / 100) % 10)
        self.afficherChiffre(756, int(score / 10) % 10)
        self.afficherChiffre(805, score % 10)

    # ------------------------------------------------------------------------
    # afficher un chiffre

    def afficherChiffre(self, position, chiffre):
        if chiffre == 0:
            self.afficherImage(position, 228, self.imgChiffre0)
        elif chiffre == 1:
            self.afficherImage(position, 228, self.imgChiffre1)
        elif chiffre == 2:
            self.afficherImage(position, 228, self.imgChiffre2)
        elif chiffre == 3:
            self.afficherImage(position, 228, self.imgChiffre3)
        elif chiffre == 4:
            self.afficherImage(position, 228, self.imgChiffre4)
        elif chiffre == 5:
            self.afficherImage(position, 228, self.imgChiffre5)
        elif chiffre == 6:
            self.afficherImage(position, 228, self.imgChiffre6)
        elif chiffre == 7:
            self.afficherImage(position, 228, self.imgChiffre7)
        elif chiffre == 8:
            self.afficherImage(position, 228, self.imgChiffre8)
        elif chiffre == 9:
            self.afficherImage(position, 228, self.imgChiffre9)

    # ------------------------------------------------------------------------
    # afficher une image sur l'image de fond d'écran

    def afficherImage(self, x, y, image):
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.ecran.blit(image, rect)

    # ------------------------------------------------------------------------
    # restaurer en mémoire l'image de fond d'écran (ceci provoque
    # l'effacement de tous les personnages)

    def effacerImageInterne(self):
        self.ecran.blit(self.imgFondEcran, (0, 0, 897, 792), (0, 0, 897, 792))

    # ------------------------------------------------------------------------
    # rendre l'image du jeu en mémoire visible à l'écran

    def actualiserFenetreGraphique(self):
        pygame.display.update()
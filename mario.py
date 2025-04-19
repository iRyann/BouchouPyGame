import pygame
from constantes import *

class Mario:
    def __init__(self):
        self.position = 0
        self.ligne = 4
        self.etat = Constantes.NORMAL
        self.delai = 1

    def reset(self, stayAtPosition=False):
        if not stayAtPosition:
            self.position = 0
            self.ligne = 4
        self.etat = Constantes.NORMAL
        self.delai = 1

    def actualiser(self, evenement):
        self.delai -= 1

        if self.delai == 0:
            self.delai = 1
            self.etat = Constantes.NORMAL

            if self.ligne == 4:
                if evenement == pygame.K_LEFT:
                    if self.position > 0:
                        self.position -= 1
                elif evenement == pygame.K_RIGHT:
                    if self.position < 8:
                        self.position += 1
                elif evenement == pygame.K_UP:
                    if self.position == 8:
                        self.ligne = 3
                elif evenement == pygame.K_SPACE:
                    if self.position in [0, 6]:
                        self.etat = Constantes.SAUT
                        self.delai = 12
            elif self.ligne == 3:
                if evenement == pygame.K_LEFT:
                    if self.position > 0:
                        self.position -= 1
                elif evenement == pygame.K_RIGHT:
                    if self.position < 8:
                        self.position += 1
                elif evenement == pygame.K_UP:
                    if self.position == 0:
                        self.ligne = 2
                elif evenement == pygame.K_SPACE:
                    if self.position in [4, 5, 6]:
                        self.etat = Constantes.SAUT
                        self.delai = 12
            elif self.ligne == 2:
                if evenement == pygame.K_UP:
                    self.ligne = 1
                elif evenement == pygame.K_DOWN:
                    self.ligne = 3
            elif self.ligne == 1:
                if evenement == pygame.K_UP:
                    self.ligne = 0
                elif evenement == pygame.K_DOWN:
                    self.ligne = 2
            elif self.ligne == 0:
                if evenement == pygame.K_LEFT:
                    if self.position > 0:
                        self.position -= 1
                elif evenement == pygame.K_RIGHT:
                    if self.position < 2:
                        self.position += 1
                elif evenement == pygame.K_SPACE:
                    if self.position == 0:
                        self.etat = Constantes.LEVIER
                        self.delai = 3
                    elif self.position == 2:
                        self.etat = Constantes.SAUT
                        self.delai = 3
                elif evenement == pygame.K_DOWN:
                    if self.position == 0:
                        self.ligne = 1
                
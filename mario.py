import pygame
from constantes import *

class Mario:
    def __init__(self):
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
                    print("à implémenter ...")
                elif evenement == pygame.K_SPACE:
                    print("à implémenter ...")
            elif self.ligne == 3:
                print("à implémenter ...")
            elif self.ligne == 2:
                print("à implémenter ...")
            elif self.ligne == 1:
                print("à implémenter ...")
            elif self.ligne == 0:
                print("à implémenter ...")
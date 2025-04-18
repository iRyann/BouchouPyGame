from presentation import *
from mario import *
from timerBarres import *
from barre import *

class Jeu:
    def __init__(self):
        self.presentation = Presentation() 
        self.mario = Mario() 
        self.timerBarres = TimerBarres()
        self.bars = []
        self.echecCount = 0

    # ----------------------------------------------------------------------------
    # Méthode contenant la boucle principale du jeu

    def demarrer(self):
        while True: 

            # récupérer l'événement du joueur et changer l'état de Mario
            self.mario.actualiser(self.presentation.lireEvenement())
            
            # Gérer les barres
            if self.timerBarres.actualiser(self.presentation.lireEvenement()):
                self.bars.append(Barre())
            
            for barre in self.bars:
                barre.actualiser(self.presentation.lireEvenement())
                if barre.state == Constantes.TERMINE:
                    self.bars.remove(barre)
            
            # Détecter les collisions entre Mario et les barres
            self.collider()
            
            # Mettre à jour l'image à l'écran
            self.actualiserEcran()

            # attendre 100 millisecondes (délai de référence)

            time.sleep(0.1)

    # ----------------------------------------------------------------------------
    # mettre à jour l'image à l'écran

    def actualiserEcran(self):
        self.presentation.effacerImageInterne()

        self.presentation.afficherMario(self.mario.ligne, self.mario.position,
                                        self.mario.etat)
        for barre in self.bars:
            self.presentation.afficherBarre(barre.position)

        self.presentation.afficherEchecs(self.echecCount)
        if(self.echecCount == 3):
            self.presentation.effacerImageInterne()
            self.presentation.attendreFermetureFenetre()

        self.presentation.actualiserFenetreGraphique()

    def collision(self):
        time.sleep(0.5)
        self.echecCount += 1
        self.mario.reset()

    def collider(self):
        if self.mario.ligne == 2 :
            for barre in self.bars:
                if barre.position == 0:
                    self.collision()
                    break
        elif self.mario.ligne == 3 and self.mario.etat == Constantes.SAUT:
            for barre in self.bars:
                if barre.position == self.mario.position:
                    self.collision()
                    break



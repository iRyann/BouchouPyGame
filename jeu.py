from presentation import *
from mario import *
from timerBarres import *

class Jeu:
    def __init__(self):
        self.presentation = Presentation() 
        self.mario = Mario() 
        self.timerBarres = TimerBarres()
        self.bars = []

    # ----------------------------------------------------------------------------
    # Méthode contenant la boucle principale du jeu

    def demarrer(self):
        while True: 
            # récupérer l'événement du joueur et changer l'état de Mario
	
            self.mario.actualiser(self.presentation.lireEvenement())

            if self.timerBarres.actualiser(self.presentation.lireEvenement()):
                pass
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

        self.presentation.actualiserFenetreGraphique()


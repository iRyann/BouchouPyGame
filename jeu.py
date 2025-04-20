from presentation import *
from mario import *
from timerBarres import *
from barre import *
from donkeykong import *
from grue import *
from tonneau import *

class Jeu:
    def __init__(self):
        self.presentation = Presentation() 
        self.mario = Mario() 
        self.timerBarres = TimerBarres()
        self.bars = []
        self.echecCount = 0
        self.donkeyKong = DonkeyKong()
        self.grue = Grue()
        self.nbCrochets = 4
        self.points = 0
        self.casks = []
    # ----------------------------------------------------------------------------
    # Méthode contenant la boucle principale du jeu

    def demarrer(self):
        while True: 
            
            if self.echecCount >= 3:
                self.presentation.attendreFermetureFenetre()

            # récupérer l'événement du joueur et changer l'état de Mario
            self.mario.actualiser(self.presentation.lireEvenement())
            if(self.donkeyKong.actualiser(self.presentation.lireEvenement())):
                self.casks.append(Tonneau(self.donkeyKong.position))
            
            # Gérer les barres
            if self.timerBarres.actualiser(self.presentation.lireEvenement()):
                self.bars.append(Barre())
            
            for barre in self.bars:
                barre.actualiser(self.presentation.lireEvenement())
                if barre.state == Constantes.TERMINE:
                    self.bars.remove(barre)
            
            # Détecter les collisions entre Mario et les barres
            self.collider()

            # Gérer les tonneaux
            for cask in self.casks:
                cask.actualiser(self.presentation.lireEvenement())
                if cask.etat == Constantes.TERMINE:
                    self.casks.remove(cask)
            
            self.cask_collider()

            self.cask_mario_collider()

            # Gérer la grue
            self.grue.actualiser(self.presentation.lireEvenement())

            if(self.mario.etat == Constantes.LEVIER and self.grue.state == Constantes.TERMINE):
                self.grue.state = Constantes.NORMAL
            # elif(self.mario.etat == Constantes.LEVIER and self.grue.state == Constantes.NORMAL):
            #     self.grue.state = Constantes.TERMINE
            
            if(self.grue.state == Constantes.NORMAL and self.grue.position == 0 and self.mario.etat == Constantes.SAUT and self.nbCrochets > 0):
                self.nbCrochets -= 1
                self.points += 5
                if(self.nbCrochets == 0):
                    for i in range(1, 6):
                        self.actualiserEcran(False, seqNum=0, sucNum=i)
                        time.sleep(0.2)
                    self.victory()
                else:
                    for i in range(1, 4):
                        self.actualiserEcran(False, seqNum=0, sucNum=i)
                        time.sleep(0.2)
                    self.mario.reset()
            elif(((self.grue.state == Constantes.NORMAL and self.grue.position != 0) or self.grue.state == Constantes.TERMINE) and self.mario.etat == Constantes.SAUT and self.mario.ligne == 0):
                self.echecCount += 1
                for i in range(1, 3):
                    self.actualiserEcran(False, seqNum=i)
                    time.sleep(0.2)
                time.sleep(0.3)
                self.mario.reset()
                    
            # Mettre à jour l'image à l'écran
            self.actualiserEcran()

            # attendre 100 millisecondes (délai de référence)
            time.sleep(0.1)

    # ----------------------------------------------------------------------------
    # mettre à jour l'image à l'écran

    def actualiserEcran(self, usual = True, seqNum = 0, sucNum = 0):
        self.presentation.effacerImageInterne()
        
        if(usual):
            self.presentation.afficherMario(self.mario.ligne, self.mario.position,
                                        self.mario.etat)
        else:
            if seqNum != 0:
                self.presentation.afficherMarioEchec(seqNum)
            elif self.nbCrochets > 0:
                self.presentation.afficherMarioSucces(sucNum)
            elif self.nbCrochets == 0:
                self.presentation.afficherMarioSuccesDK(sucNum)

        if(self.nbCrochets > 0):
            self.presentation.afficherDonkeyKong(self.donkeyKong.position, self.donkeyKong.state)
        
        for barre in self.bars:
            self.presentation.afficherBarre(barre.position)
        
        for cask in self.casks:
            self.presentation.afficherTonneau(cask.ligne, cask.position)
        
        self.presentation.afficherLevier(self.grue.state)
        
        self.presentation.afficherGrue(self.grue.position, self.grue.state)

        self.presentation.afficherEchecs(self.echecCount)

        self.presentation.afficherScore(self.points)
        self.presentation.afficherEchafaudage(self.nbCrochets)
    
        self.presentation.actualiserFenetreGraphique()

    def collision(self):
        time.sleep(0.5)
        self.echecCount += 1
        for cask in self.casks:
            if cask.ligne == 6 and cask.position in [1, 2, 3]:
                self.casks.remove(cask)
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
    
    def cask_collider(self):
        positions_ligne3 = {cask.position+1 for cask in self.casks if cask.ligne == 3}
        for cask in self.casks:
            if cask.ligne == 2 and cask.position in positions_ligne3:
                self.casks.remove(cask)

    def cask_mario_collider(self):
        bias = {
            0: -1,
            1: 0,
            2: -1,
            3: 1,
            4: -1,
            5: 3,
            6: 4
        }
        for cask in self.casks:
            if bias[cask.ligne]  == self.mario.ligne :
                if (bias[cask.ligne] == 0 and cask.position == self.mario.position) \
                or (bias[cask.ligne] == 1 and cask.position == 1) \
                or (bias[cask.ligne] == 3 and cask.position-1 == self.mario.position) \
                or (bias[cask.ligne] == 4 and cask.position == self.mario.position + 1):
                    if self.mario.etat == Constantes.SAUT:
                        self.points += 1
                    else:
                        self.collision()       
                
    
    def victory(self):
        self.mario.reset()
        self.nbCrochets = 4
        self.points = 0
        self.echecCount = 0
        self.bars = []
        self.timerBarres.reset()



from constantes import Constantes
from random import randint
class DonkeyKong:
    def __init__(self):
        self.position = 0
        self.delay = 6
        self.state = Constantes.NORMAL
        self.tonneauDelay = 42
    
    def actualiser(self, event):
        self.delay -= 1
        self.tonneauDelay -= 1


        if self.delay == 0:
            self.delay = 6
            self.state = Constantes.NORMAL
            
            gap = randint(-1,1)
            while self.position + gap not in [0,1,2]:
                gap = randint(-1,1)
            self.position += gap
            
        if self.tonneauDelay == 0:
            self.tonneauDelay = randint(40, 54)
            self.state = Constantes.TONNEAU
            self.delay = 6
            return True
        
        return False


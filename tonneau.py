from constantes import Constantes

class Tonneau:
    def __init__(self, dk_position):
        self.position = dk_position
        self.ligne = 0
        self.etat = Constantes.NORMAL
        self.delai = 6
    
    def actualiser(self, event):
        self.delai -= 1

        if self.delai == 0:
            self.delai = 6
            self.etat = Constantes.NORMAL

            if self.ligne in [0, 1, 2]:
                self.ligne += 1
                if self.ligne == 3:
                    self.position += 3
            elif self.ligne == 3:
                if self.position > 0:
                    self.position -= 1
                else:
                    self.ligne = 4
            elif self.ligne == 4:
                self.ligne = 5
                self.position = 0
            elif self.ligne == 5:
                if self.position < 10:
                    self.position += 1
                else:
                    self.ligne = 6
                    self.position = 10
            elif self.ligne == 6:
                if self.position > 0:
                    self.position -= 1
                else:
                    self.etat = Constantes.TERMINE




        

    
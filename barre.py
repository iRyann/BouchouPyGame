from constantes import *

class Barre:
    def __init__(self):
        self.delay = 12
        self.state = Constantes.NORMAL
        self.position = 8


    def actualiser(self, event):
        self.delay -= 1

        if self.delay == 0:
            self.delay = 12

            if self.position > 0:
                self.position -= 1
            else:
                self.state = Constantes.TERMINE

   
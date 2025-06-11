from constantes import Constantes

class Grue:
    def __init__(self):
        self.delay = 6
        self.state = Constantes.TERMINE
        self.position = 0
        self.rise = True
        self.activeDelay = 150

    def actualiser(self, event):

        if self.state == Constantes.NORMAL:
            self.delay -= 1
            self.activeDelay -= 1

        if self.activeDelay == 0:
            self.activeDelay = 50
            self.state = Constantes.TERMINE
            self.position = 0
            self.rise = True

        if self.delay == 0:
            self.delay = 6
            

            if self.position < 4 and self.rise:
                self.position += 1
            elif self.position == 4:
                self.rise = False
                self.position -= 1
            elif self.position > 0 and not self.rise:
                self.position -= 1
            elif self.position == 0:
                self.rise = True
                self.position += 1
            
            
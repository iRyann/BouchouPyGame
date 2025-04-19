from random import randint

class TimerBarres:
    def __init__(self):
        self.delai = 85
        self.new_time = 500
        self.current_delai = 85
        
    def actualiser(self, evenement):
        self.delai -= 1
        self.new_time -= 1

        if self.delai <= 0:
            if(self.new_time <= 0):
                self.new_time = 500
                self.current_delai = randint(70,100)
            
            self.delai = self.current_delai
            return True
        else:
            return False
    
    def reset(self):
        self.delai = 85
        self.new_time = 500
        self.current_delai = 85
class Turnmaster:
    def __init__(self, entities):
        self.entities = entities
        self.turn = 0

    def vezdequem(self):
        return self.entities[self.turn]
    
    def passarturno(self):
        self.turn+=1
        if self.turn >= len(self.entities):
            self.turn = 0

    def removermortos(self):
        self.entities = [e for e in self.entities if e.acthp > 0]
        if self.turn >= len(self.entities):
            self.turn= 0
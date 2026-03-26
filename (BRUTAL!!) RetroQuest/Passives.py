#definindo passivas
class passive:
    def __init__(self, name, description, effect): #adicionar "TRIGGER" depois
        self.basename= name
        self.level=1
        self.description=description
        self.effect=effect
    def passiveactivationtrigger(self):
        pass

    def nome_modificado(self):
        return f"{self.basename} Lv {self.level}"
    def level_up(self):
        self.level+=1
        print(f"{self.basename} leveled up to Lv {self.level}!")
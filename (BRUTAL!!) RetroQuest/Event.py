from Commands import input_player

class event:
    def __init__(self, name, text, effect=None):
        self.name=name
        self.text=text
        self.effect=effect

    def trigger(self, player):
        #apresentação do evento
        print(f"EVENT: {self.name}")
        print(self.text)
        #efeito do evento
        if self.effect:
            self.effect(player)
        while True:
            choice = input_player(player,None)
            if choice == "ok":
                    break
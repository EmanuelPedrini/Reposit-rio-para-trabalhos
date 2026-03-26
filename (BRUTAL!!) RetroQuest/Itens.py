class item:
    def __init__(self, name, slot, bonus):
        self.name = name
        self.slot = slot
        self.bonus = bonus

class armor:
    def __init__(self, name, acmath):
        self.name=name
        self.slot = "Armor"
        self.acmath = acmath

class usableitem:
    def __init__(self, name, uses, damageg, healg, manag, centsg, xpg):
        pass
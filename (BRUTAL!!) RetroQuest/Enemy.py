import random
from Globals import *
from utils import rolld20
from Itens_Data import todososequipamentos

# from 
class enemy:
    def __init__(self, name, totalmaxhp, atk, atkbonus, vampirism, thorns, ac, centsondeath, xpondeath):
        self.name = f"{name} / [ Level {globaldanger }  ]"
        #hp
        self.totalmaxhp = int(round(totalmaxhp * globaldangercalc))
        self.acthp = self.totalmaxhp

        #escala
        self.atkbonus = int(atkbonus * (1 * globaldangercalc))
        self.atk = int(round(atk * globaldangercalc))
        self.ac = int(round(ac + (2 * globaldangercalc)))
        self.centsondeath = int(centsondeath)
        self.xpondeath = int(xpondeath)

        #secondary atributes
        self.vampirism=vampirism
        self.realvampirism=float(vampirism*0.01)
        self.thorns=thorns

        #self.dead=False
    #Ancora 3

    def toma(self, damage, player):
        self.acthp -= damage
        self.death(player)

    def heal(self, amount):
        self.acthp += amount
        if self.acthp > self.totalmaxhp:
            self.acthp = self.totalmaxhp
        print(f"> the enemy {self.name} healed [ {amount} ] Hp")

    def attack(self, player):
        roll= rolld20() + self.atkbonus
        if roll >= player.ac:
            damage = self.atk
            if self.vampirism != 0:
                self.heal(int(damage*(self.realvampirism)))
            print(f"[ {roll} ]! {self.name} hit the {player.name} dealing {damage} damage!")
            player.toma(damage)
        else:
             print(f"{self.name} missed a attack against the {player.name}!")
    

    def death(self, player):
        if self.acthp <= 0:
            centsg = int(random.randint(self.centsondeath, self.centsondeath*3) * (1 + globaldanger   * 0.4))
            xpg = int(random.randint(self.xpondeath, self.xpondeath*3) * (1 + globaldanger   * 0.6))

            randomitemgain=random.randint(1, 100) + player.luck
            if randomitemgain <= 50:
                maxitemgain=1
            elif randomitemgain <= 85:
                maxitemgain=2
            else:
                maxitemgain=3
            
            maxitemgain = min(maxitemgain, len(todososequipamentos))

            itemg = random.sample(todososequipamentos, maxitemgain)

            print(f"the {self.name} died!")

            player.gain_cents(centsg)
            player.gain_xp(xpg)
            for item in itemg:
                player.add_item(item)
            
            return True
        return False

import random
from utils import rolld20
import sys

class character:
    def __init__(self, name, pronoun, possessive, strg, dex, vit, luck, cha, intel, ac, vampirism, thorns, armor, skills, passives, cents):
        #textos
        self.name = name 
        self.pronoun = pronoun
        self.possessive = possessive

        #atkbonus, perguntar pro akira se isso aqui é necessário
        self.rollbonus = 0
        self.atkdmgbonus = 0
        self.temprollbonuscombat = 0
        self.tempatkdmgbonuscombat = 0
        self.temprollbonusturn = 0
        self.tempatkdmgbonusturn = 0

        #estados (não do brasil, lengo lengo lengo)
        self.stunned = False

        self.ac= ac

        #atributes
        self.strg = int(strg)
        self.dex = int(dex)
        self.vit = int(vit)
        self.luck = int(luck)
        self.cha = int(cha)
        self.intel=int(intel)

        #secondary atributes
        self.vampirism=vampirism
        self.realvampirism=float(vampirism*0.01)
        self.thorns=thorns
        self.armor=armor
        #terminar
        # self.shield=self.shield
        # self.shieldstat=self.shield

        #level system
        self.level=int(1)
        self.xp=int(0)
        self.xptonext=int(100)

        #calculo de hp maximo
        self.bonushp=0
        self.maxhp= 5 * self.vit
        self.totalmaxhp = self.maxhp + self.bonushp
        self.acthp = self.totalmaxhp

        #inventory system
        #inventario é so uma big lista anota ai
        self.inventory =[]

        self.equipments = {
            "Weapon": None,
            "Armor": None,
            "Accessory": None,
        }

        #skills pqp
        self.skills= skills
        self.passives = passives
        self.maxskills = 4
        self.maxpassives = 2

        #dineiro
        self.cents=int(cents)

        #mana
        self.maxmana = 5 * self.cha
        self.manaregen = self.intel
        self.manainicial = self.cha
        self.actmana = self.manainicial
    
    #definições de sistema de Inventário
    def add_item(self, item):
            self.inventory.append(item)
            print(f"> You obtained {item.name}!")

    def remove_item(self, item):
            if item in self.inventory:
                self.inventory.remove(item)
                print(f"> {item.name} got removed from your inventory!")
            else:
                print("> That item isn`t in your inventory")

    def equip(self,item):
        #so muda slot pra slot do item em questão
        slot = item.slot
        #removendo item se ja tem algo equipado
        if self.equipments[slot] is not None:
            retirado = self.equipments[slot]
            self.inventory.append(retirado)
            print(f"> You unequipped [ {retirado.name} ]!")
        self.equipments[slot] = item
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"> Equipped {item.name}")

        #regenerar mana
    def regen_mana(self):
        self.actmana += self.manaregen
        print(f"{self.name} regenerated {self.manaregen} Mana Points!")
        if self.actmana > self.maxmana:
            self.actmana = self.maxmana

        #ganhar mana != regenerar mana
    def gain_mana(self, amount):
        self.actmana += amount
        if self.actmana > self.maxmana:
            self.actmana = self.maxmana
        print(f"{self.name} obtained {amount} Mana Points! \nNow {self.pronoun} have [ {self.actmana} / {self.maxmana} ] Mana Points")

    def mana_use(self, amountused):
        if self.actmana >= amountused:
            print(f"You actually have [ {self.actmana} / {self.maxmana} ] Mana Points! This is enough to cast this Ability!")
            self.actmana -= amountused
            print(f"Now you have [ {self.actmana} / {self.maxmana} ] Mana Points!")
        else:
            print(f"You actually have [ {self.actmana} / {self.maxmana} ] Mana Points! This isn`t enough to cast this Ability!")

    def rollbonusforbasicatt(self):
         return self.strg + self.rollbonus

    def gain(self, attr, amount):
        setattr(self, attr, getattr(self, attr) + amount)
    def lose(self, attr, amount):
        setattr(self, attr, getattr(self, attr) - amount)
    
    #BASIC ATTACK
    def basicattack(self, target, player):
            #rola o Dado
            roll = rolld20() + self.rollbonusforbasicatt()
            if roll >= target.ac:
                #Computa o Dano
                randomdmg = random.randint(int(0.5 * self.strg), self.strg)
                damage = randomdmg + self.atkdmgbonus

                #Mostra o dano e causa o dano ao inimigo
                print(f"> The [ {self.name} ] HIT! {self.pronoun} rolled [ {roll} ]! dealing [ {damage} ( {randomdmg} + {self.atkdmgbonus} ) ] DAMAGE to [ {target.name} ]")
                target.toma(damage, player)

                #Computa o tanto que tu curo com o ataque
                if self.vampirism != 0:
                    player.heal(int(damage*(self.realvampirism)))
                
                if target.thorns != 0:
                    Espinhado= int(target.thorns)
                    player.toma(int(Espinhado))
                    print(f"> You taked [ {Espinhado} ] damage from the enemy thorns!")
                
                # if target.
                if target.acthp <= 0:
                    return
            else:
                print(f"You missed {target.name}, you rolled [ {roll} ] !")

    def toma(self, damage):
        self.acthp -= damage
        self.death()

    def heal(self, amount):
        self.acthp += amount
        if self.acthp > self.totalmaxhp:
            self.acthp = self.totalmaxhp
        print(f"> {self.name} healed [ {amount} ] Hp")
    
    def gain_xp(self, xpamount):
        self.xp+=xpamount
        print(f"> {self.name} gained {xpamount} xp!")
        self.level_system()

    def gain_cents(self, amount):
        self.cents+=amount
        print(f"> {self.name} gained {amount} cents!")

    def lose_cents(self, amount):
        self.cents -=amount
        print(f"> {amount} cents got away from your wallet!")

    def level_system(self):
        if self.xp>=self.xptonext:
            self.xp -= self.xptonext
            self.level +=1
            print(f"> The {self.name}  leveled up! Now {self.pronoun} is level {self.level}!")
            self.level_up_rewards()
            self.xptonext = int(100 * (1.5 ** (self.level - 1)))

    Attribute_rewards = [
    ("+2 Strength", lambda p: p.gain("strg", 2)),
    ("+2 Vitality", lambda p: p.gain("strg", 2)),
    ("+2 Dexterity", lambda p: p.gain("strg", 2)),
    ("+2 Charisma", lambda p: p.gain("strg", 2)),
    ("+2 Luck", lambda p: p.gain("strg", 2)),
    ("+2 Intelligence", lambda p: p.gain("strg", 2)),

    ]
    
    def level_up_rewards(self):
        pass
        #     #amostra total que tu pode receber
        # options=[]

        # #tu pode receber (la ele)
        # canskills = len(self.skills) < self.maxskills
        # canpassives = len(self.passives) < self.maxpassives

        # #definindo se tu pode receber passivas
        # if canpassives:
        #     options += random.sample(todasaspassivas, min (3, len(todasaspassivas)))
        # #mema traquera mas comm skills
        # if canskills:
        #     option += random.sample(todasskills, min (3, len(todasskills)))

        # #receba tributos
        # if not canpassives and not canskills:
        #     options = random.sample(self.Attribute_rewards, 3)

        pass
    def death(self):
        if self.acthp<=0:
            print(f"the {self.name} got killed by a enemy and died in a horrible way!")
            sys.exit()
        
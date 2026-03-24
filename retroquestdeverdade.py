import random; import sys; import copy;
def rolld20():
    return int(random.randint(1,20))

def rolld6():
    return int(random.randint(1,6))

def mult_rolld6(numdice):
    total=0
    for i in range(numdice):
        total +=random.randint(1, 6)
    return int(total)

globaldanger = 1
globaldangercalc = (0.5*(globaldanger + 1))
gamerunning = 1

class skill:
    def __init__(self, name, description, damage, heal, cost):
          self.basename = name
          self.level=1
          self.description=description
          self.damage=damage
          self.cost=cost
          self.heal=heal
    def nome_modificado(self):
        return f"{self.basename} Lv {self.level}"
    def level_up(self):
        self.level+=1
        print(f"{self.basename} leveled up to Lv {self.level}!")

    def use(self, player, target):
            if not player.mana_use(self.cost):
                return False
            damage = self.damage
            if self.damage != 0:
                    target.toma(self.damage)
                    print(f"{player.name} used {self.basename} and caused {damage} damage to {target.name}!")
            if self.heal != 0:
                    player.heal(self.heal)
            return True

class item:
    def __init__(self, name, slot, bonus):
        self.name = name
        self.slot = slot
        self.bonus = bonus

#weapons
rustysword=item("Rusty sword", "Weapon", 0)
iron_sword = item("Iron Sword", "Weapon", 3)
butchers_cleaver = item("Butcher's Cleaver", "Weapon", 5)

#lista com todas as weapons
todasaarmas=[rustysword, iron_sword, butchers_cleaver]

#armors
torn_clothes = item("Torn Clothes", "Armor", 1)
leather_armor = item("Leather Armor", "Armor", 3)
chainmail = item("Chainmail", "Armor", 5)

#lista com todas as armaduras
todasasarmors=[torn_clothes, leather_armor, chainmail]

#acsessories
old_ring = item("Old Ring", "Accessory", 1)
mana_pendant = item("Mana Pendant", "Accessory", 2)
lucky_charm = item("Lucky Charm", "Accessory", 3)

#lista com todos
todososacesssorios=[old_ring, mana_pendant, lucky_charm]

#lista com todos os equipamentos
todososequipamentos = todasaarmas + todososacesssorios + todasasarmors


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

#passivas
brutamontes= passive("Brute", "You dont fear Anyone, you gain", 0 )
assassin= passive("Assassin", "You blablabla", 0)
parede = passive("Human Wall", "Galhofinhas", 0)
incansavel= passive("Tireless", "Gugu dada", 0)

#lista de passivas
todasaspassivas =[brutamontes, assassin, parede, incansavel]

#skills
fireball=skill("Fireball", "You cast a giant fireball to destroy your enemies!", 10, 0, 8)
healing= skill("Healing", "You heal your wounds", 0, 5, 4)
satorogojonaooooo= skill("Deep Purple", "GOJO NOOOO", 15, 0, 12)
manaflow=skill("Mana Flow", f"you use all your actual mana ({0}) and heal a equivalent amount.", 0, 0, 0)
lightning=skill("Lightning", "Balls", 4, 0, 3)

#lista de todas as skills
todasskills=[fireball,healing,satorogojonaooooo,manaflow,lightning]

#ANCORA 2
class character:
    def __init__(self, name, pronoun, possessive, strg, dex, vit, luck, cha, intel, ac, skills, passives, cents):
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

        #estados (não do brasil, lengo lengo
        self.stunned = False

        #atributes
        self.ac= ac
        self.strg = int(strg)
        self.dex = int(dex)
        self.vit = int(vit)
        self.luck = int(luck)
        self.cha = int(cha)
        self.intel=int(intel)

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
            print(f"> Equipped {item.name}!")

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
            print(f"You actually have [ {self.actmana} / {self.maxmana} ] Mana Points! This is enough to cast this Ability!\nNow you have [ {self.actmana} / {self.maxmana} ] Mana Points! ")
            self.actmana -= amountused
            return True
        else:
            print(f"You actually have [ {self.actmana} / {self.maxmana} ] Mana Points! This isn`t enough to cast this Ability!")
            return False

    def rollbonusforbasicatt(self):
         return self.strg + self.rollbonus

    def gain(self, attr, amount):
        setattr(self, attr, getattr(self, attr) + amount)
    def lose(self, attr, amount):
        setattr(self, attr, getattr(self, attr) - amount)
    
    #BASIC ATTACK
    def basicattack(self, target):
            roll = rolld20() + self.rollbonusforbasicatt()
            if roll >= target.ac:
                randomdmg = random.randint(int(0.5 * self.strg), self.strg)
                damage = randomdmg + self.atkdmgbonus
                target.toma(damage)
                if target.acthp <= 0:
                    return
                print(f"> The [ {self.name} ] HIT! {self.pronoun} rolled [ {roll} ]! dealing [ {damage} ( {randomdmg} + {self.atkdmgbonus} ) ] DAMAGE to [ {target.name} ]")
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
            print(f"the {self.name} got killed by {actenemy.name} and died in a horrible way!")
            sys.exit()
        
class enemy:
    def __init__(self, name, totalmaxhp, atk, atkbonus, ac, centsondeath, xpondeath):
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

        #self.dead=False
    #Ancora 3
    def attack(self, player):
        roll= rolld20() + self.atkbonus
        if roll >= player.ac:
            damage = self.atk
            player.toma(damage)
            print(f"[ {roll} ]! {self.name} hit the {player.name} dealing {damage} damage!\n")
        else:
             print(f"{self.name} missed a attack against the {player.name}!")

    def toma(self, damage):
        self.acthp -= damage
        self.death()

    def death(self):
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
            choice = input_player(player,enemy=None)
            if choice == "ok":
                    break
#eventos neutros
mercador=event("Merchant", "You encounter a small man in a black cape with a enormous backpack, he looks like some kind of merchant.")

neutralevents=[mercador]

#eventos ruins
pisadaemarmadilha=event("placeholder", "placeholder")

badevents=[pisadaemarmadilha]

#eventos bons
fontedecura = event("placeholder", "placeholder")

goodevents=[fontedecura]

#enemies
fluffyskeleton=enemy("Fluffy`s Skeleton", 20, 5, 0, 12,3, 30)
undeadgrandma=enemy("Undead Grandma", 30, 3, 0, 12,3, 30)
dasbinich=enemy("DAS BIN ICH?!!", 25, 4, 1, 10,3, 30)
unthought=enemy("Unthought", 15, 7, 2, 14,3, 30)


enemies_pool =[fluffyskeleton, undeadgrandma, dasbinich, unthought]
print("Welcome to retroquest! if want to stop the game, type [EXIT] ")

def lookyourteeth_command(player=None, enemy=None):
    print(f"\n=== {player.name} STATS ===")
    print(f"Health Points   : [ {player.acthp} / {player.totalmaxhp} ]")
    print(f"Mana Points : [ {player.actmana} / {player.maxmana} ]")
    print(f"Attributes:")
    print(f"STR : {player.strg}")
    print(f"DEX : {player.dex}")
    print(f"VIT : {player.vit}")
    print(f"INT : {player.intel}")
    print(f"CHA : {player.cha}")
    print(f"LUCK: {player.luck}")

def showinventory_command(player=None, enemy=None):
    for i, item in enumerate(player.inventory):
        print(f"[ {i+1} ] - {item.name}")
    if player.inventory==[]:
        print("> You don`t have any item in your inventory.")

def exam_enemy_command(player=None, enemy=None):
        for e in actenemy:
            if e.acthp > 0:
                print(f"- {e.name} ( {e.acthp} / {e.totalmaxhp} HP )")
def look_wallet_command(player=None, enemy=None):
    print(f"You actually have {player.cents} cents!")

def Devconsole_FullHealth_Command(player=None, enemy=None):
    player.heal(player.totalmaxhp)
    print("You healed to full now, cheater.")

def Devconsole_InstaKillEnemy_Command(player=None, enemy=None):
    if not actenemy:
        print("No enemies to erase")
        return
    target = escolhadealvo(player, actenemy)
    target.toma(9999999999999999999999999999999999)
    print(f"{target.name} got ERASED!")

def Devconsole_InstaKillAllEnemies_command(player=None, enemy=None):
    if not actenemy:
        print("No enemies to erase")
        return
    for e in actenemy:
        e.toma(999999999999999999999999999999999999)
        print(f"{e.name} got ERASED!")

def Devconsole_Eventchange(player=None, enemy=None):
    pass

def Devconsole_AddSkill_Command(player=None, enemy=None):
    skilldevadd = input(f"Please, input the NAME of the skill.\n> ")
    for s in todasskills:
        if skilldevadd == s.basename:
            player.skills.append(s) 
            print(f"Added {skilldevadd} to your actualturn skills!")
            return
    print(f"{skilldevadd} don`t exist in the skill list, incorrect typing or non existent.")

def Devconsole_ShowAllskills_Command(player=None, enemy=None):
    print("Skills:")
    for s in todasskills:
        print("-", s.basename)
    
def removeitemfrominventory_command(player=None, enemy=None):
    #mostra o inventário
    for i, item in enumerate(player.inventory):
        print(f"[ {i+1} ] - {item.name}")
    if player.inventory==[]:
        print("You don`t have any item in your inventory.")
        return
    #pede qual o item
    itemretirado= input("Please, input the NAME of the item you want to remove.")
    # executa a ação de retirar o item
    for s in player.inventory:
        if itemretirado == s.name:
            player.remove_item(s)
            print(f"{itemretirado} got removed from your inventory.")
            return
    print("This item ins`t in your inventory.")

def EXIT_command(player=None, enemy=None):
    print("Bye Bye, Friend!")
    sys.exit()

comandosglobais={
    "lookteeths" : lookyourteeth_command,
    "lk": lookyourteeth_command,
    "examenemy": exam_enemy_command,
    "exen": exam_enemy_command,
    "lookwallet": look_wallet_command,
    "lkw": look_wallet_command,
    "showinventory": showinventory_command,
    "devconsolefullhealth": Devconsole_FullHealth_Command,
    "EXIT": EXIT_command,
    "devconsoleaddskill": Devconsole_AddSkill_Command,
    "devconsoleshowskilllist": Devconsole_ShowAllskills_Command,
    "removeitem" : removeitemfrominventory_command,
    "devconsoleeraseenemy" : Devconsole_InstaKillEnemy_Command,
    "devconsoleeraseallenemies": Devconsole_InstaKillAllEnemies_command
}

# negocio para ler input sempe
def input_player(player, enemy=None):
    while gamerunning==1:
        comando = input("> ")
        if comando in comandosglobais:
            comandosglobais[comando](player, enemy)
            continue
        return comando
    else:
        print("invalid")

#characters
Knight = character("Knight","she","her", 10, 2, 5, 0, 3, 3, 10, [healing], [], 0 )
Mage = character("Mage","he", "his", 3, 3, 3, 1, 5, 5, 10, [fireball], [], 5)

def character_choice():
    while True:
     print("Choose your character!")
     print("Type [1] for the Knight, strong and durable!")
     print("Type [2] for the Mage, the master of strategy!")

     #escolha
     choice=input(">  ")

     if choice == "1":
        return Knight
     elif choice =="2":    
        return Mage
     else:
          print("Sorry, that's ins't a valid choice")

player = character_choice()

print(f"Congrats! You chose, the {player.name}!")

def encounter():
    quantidadeinimigos = random.randint(1, 3)
    return [
        copy.deepcopy(random.choice(enemies_pool))
        for _ in range(quantidadeinimigos)
    ]

#definições de combate
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

def escolhadealvo(player, enemies):

    alive = [e for e in enemies if e.acthp > 0]

    print("Choose target:")

    for i, e in enumerate(alive):
        print(f"[{i+1}] {e.name} ({e.acthp} HP)")

    while True:
        choice = input_player(player, None)

        if choice.isdigit():
            index = int(choice) - 1

            if 0 <= index < len(alive):
                return alive[index]

        print("Invalid target.")

def playerturn(player, enemy):
        print("> It`s Your Turn!")
        print(f"> {player.name} actually have {player.acthp}/{player.totalmaxhp} health points!")
        print(f"> You actually have [ {player.actmana} / {player.maxmana} ] Mana Points!")

        #Ações possíveis
        print("> Time to Act!\n> Actions:")
        print("[1] - BASIC ATTACK")

        for i, skill in enumerate(player.skills):
            print(f"[{i+2}] - {skill.basename}")
        ataquebasicoporturno = False

        #Escolha do player
        while True:
            choice = input_player(player, enemy=None)
            if choice =="1":
                if ataquebasicoporturno==True:
                    print("You already used your basic attack this turn!")
                    
                else: 
                        target = escolhadealvo(player, actenemy)
                        if target.acthp > 0:
                            player.basicattack(target)
                            ataquebasicoporturno=True

                        if target.acthp <= 0:
                            return
            
            elif choice.isdigit():
                #calculo pra determinar a skill na posição
                sedex= int(choice) - 2

                #verificando se o número está nas skills do PLAYER
                if 0 <= sedex < len(player.skills):
                    if skill.damage != 0:
                         target = escolhadealvo(player, actenemy)
                    else:
                        target = player

                    player.skills[sedex].use(player, target)

                    if target.acthp <= 0:
                        return

                #se n for uma skill do player, ou n estiver nas skills dele
                else:
                    print("Sorry, that is a invalid Ability.")
                    continue
            #terminando seu turno
            elif choice == "endturn" or choice == "et":
                print(f"{player.name} ended {player.possessive} turn!")
                player.regen_mana()
                break

            else:
                print("Sorry, thats a invalid Command.")
                
def enemyturn(enemy, player):
        print(f">It`s {enemy.name} TURN!\n>He (she) is going to...")
        enemy.attack(player)
        if player.acthp <=0:
            player.death()

#ANCORA 1
def combat(player, enemies):
    oncombat=[player] + enemies
    tm = Turnmaster(oncombat)

    print("TIME TO DIE!, from the tar of the void some enemies arise!")
    print("ACTION QUEUE:\n")
    for e in oncombat:
            if e.acthp > 0:
                print(f"- {e.name} ({e.acthp} / {e.totalmaxhp} HP)")
            print("")

    # for e in enemies:
    #     print(f"{e.name}")

    while True:
        tm.removermortos()

        if player.acthp <= 0:
            player.death()
            break

        if all(e.acthp <= 0 for e in enemies):
            print("Enemies are all dead!")
            break
        actualturn = tm.vezdequem()

        if hasattr(actualturn, "attack"):
            enemyturn(actualturn, player)
        else:
            playerturn(player, enemies)
        tm.passarturno()
    
while gamerunning==1:
    escolhadeevento= ((player.luck * 3 ) + random.randint(1,100))
    if escolhadeevento <= 25:
        funcdeeventruim=random.choice(badevents)
        funcdeeventruim.trigger(player)
        continue
#inimigo
    elif escolhadeevento > 25 and escolhadeevento <= 70:
         actenemy=encounter()
         combat(player, actenemy)
         continue
#neutro
    elif escolhadeevento > 70 and escolhadeevento <= 90:
         funcdeeventneutro=random.choice(neutralevents)
         funcdeeventneutro.trigger(player)
         continue
#bom
    elif escolhadeevento > 90:
        funcdeeventbom=random.choice(goodevents)
        funcdeeventbom.trigger(player)
        continue

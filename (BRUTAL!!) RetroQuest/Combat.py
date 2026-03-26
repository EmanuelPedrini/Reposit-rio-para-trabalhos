import random; import copy
from Turnmaster import Turnmaster
from Enemies_Data import enemiespool
import random
from Commands import input_player
from Commands import escolhadealvo

#definições de combate
def playerturn(player, actenemy):
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
            choice = input_player(player, actenemy)
            if choice =="1":
                if ataquebasicoporturno==True:
                    print("You already used your basic attack this turn!")
                    continue
                    
                else: 
                        target = escolhadealvo(player, actenemy)
                        if target.acthp > 0:
                            player.basicattack(target, player)
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

def combat_start(player):
    player.actmana = player.manainicial
    print("TIME TO DIE!, from the tar of the void some enemies arise!")

def combat_end():
     pass
def turn_start():
     pass
def turn_end():
     pass

#ANCORA 1
def combat(player, enemies):

    oncombat=[player] + enemies
    tm = Turnmaster(oncombat)

    combat_start(player)
    print("ACTION QUEUE:\n")
    for e in oncombat:
            if e.acthp > 0:
                print(f"- {e.name} ({e.acthp} / {e.totalmaxhp} HP)")
            print("")
            
    #essa é a parte que define o loop do combat
    while True:
        #primeiro ele usa a função que remove os inimigos mortos, ela vem do turnmaster que ta em outro arquivo
        tm.removermortos()

        #ele checa se o player morreu
        if player.acthp <= 0:
            player.death()
            break

        #checa se os inimigos morreram
        alive = [e for e in enemies if e.acthp > 0]
        if not alive:
            print("Enemies are all dead!")
            break
        
        actualturn = tm.vezdequem()
        if actualturn==player:
             playerturn(player,enemies)
        else:
             enemyturn(actualturn, player)

        tm.passarturno()
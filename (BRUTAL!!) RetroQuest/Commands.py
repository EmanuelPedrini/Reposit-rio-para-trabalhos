import sys
from Globals import gamerunning
from Skill_Data import *
from Passive_Data import *


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

def exam_enemy_command(player, actenemy):
        for e in actenemy:
            if e.acthp > 0:
                print(f"- {e.name} ( {e.acthp} / {e.totalmaxhp} HP )")
def look_wallet_command(player=None, enemy=None):
    print(f"You actually have {player.cents} cents!")

def Devconsole_FullHealth_Command(player=None, enemy=None):
    player.heal(player.totalmaxhp)
    print("You healed to full now, cheater.")

def Devconsole_InstaKillEnemy_Command(player, actenemy):
    if not actenemy:
        print("No enemies to erase")
        return
    target = escolhadealvo(player, actenemy)
    target.toma(9999999999999999999999999999999999, player)
    print(f"{target.name} got ERASED!")

def Devconsole_InstaKillAllEnemies_command(player, actenemy):
    if not actenemy:
        print("No enemies to erase")
        return
    for e in actenemy:
        e.toma(999999999999999999999999999999999999, player)
        print(f"{e.name} got ERASED!")

def Devconsole_Eventchange(player=None, enemy=None):
    pass

def Devconsole_AddSkill_Command(player=None, enemy=None):
    skilldevadd = input(f"Please, input the NAME of the skill.")
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
def input_player(player, actenemy=None):
    while gamerunning==1:
        comando = input("> ")
        if comando in comandosglobais:
            comandosglobais[comando](player, actenemy)
            continue
        return comando
    else:
        print("invalid")

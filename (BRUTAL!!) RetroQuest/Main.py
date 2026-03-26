import random; import sys; import tkinter as tk; import copy;
from Globals import gamerunning
from Combat import combat
from Events_Data import badevents, neutralevents, goodevents
from Enemies_Data import enemiespool
from Characters_Data import allcharacters
from Character import character
# from Combat import encounter

print("Welcome to retroquest! if want to stop the game, type [EXIT] ")


#characters
def character_choice():
    while True:
     print("Choose your character!")
     for i, char in enumerate(allcharacters):
            print(f"[{i+1}] - {char.name}")

     #escolha
     choice=input(">  ")

     if choice.isdigit():
         charpos=int(choice)-1
         if 0<=charpos<len(allcharacters):
             return allcharacters[charpos]
             
     else:
        print("Sorry, that's ins't a valid choice")

player = character_choice()

print(f"Congrats! You chose, the {player.name}!")
    
while gamerunning==1:
    escolhadeevento= ((player.luck * 3 ) + random.randint(1,100))
    if escolhadeevento <= 30:
        funcdeeventruim=random.choice(badevents)
        funcdeeventruim.trigger(player)
        continue
#inimigo
    elif escolhadeevento > 30 and escolhadeevento <= 70:
         quantidadeinimigos = random.randint(1, 3)
         
         actenemy = [
             copy.deepcopy(e) 
             for e in random.sample(enemiespool, k=min(quantidadeinimigos, len(enemiespool)))
         ]

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

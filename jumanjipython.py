#import pygame
import random
from random import randint
#sound=pygame.mixer.Sound("jumanji.wav")
def take(item):
    print("%s picked up %s, and the item has been put in your inventory."% (name,item))
def use(item, location):

    pass
def healthCheck(selfHealth):
    print("your health is %d" % selfHealth)


def fight(item,enemy):
    selfHealth=20
    enemyHealth=random.randint(10,20)
    damageAmountN=random.randint(5,7)
    damageAmountH=random.randint(8,10)
    damage=random.randint(0,2)
    if damage==0:
        print("%s missed! The attack did no damage and the %s had time to attack back."% (name, enemy) )
        selfHealth=selfHealth-random.randint(4,7)
        healthCheck(selfHealth)
    elif damage==1:
        print("%s's attack hit! the attack did %d damage "%(name, damageAmountN))
        enemyHealth=enemyHealth-damageAmountN
        healthCheck
    else:
        print("%s's attack hit a headshot! the attack did %d damage."%(name,damageAmountH))
        healthCheck(selfHealth)


#print('Path to module:',pygame._file_)
#pygame.mixer.Sound.play(sound)
print("Welcome to Jumanji!")
a=input("Here are your commands: [run] This lets you run away from your current location. [fight] This lets you attack any enemies you come across. [rest] this lets you sleep to regain health. [take] this lets you take an item you come across. [use] this lets you use the item you come across.  Type [Understood] if you understand. Please press space before typing.\n")
if a == " Understood":
    b= input("good. Now choose your character. [Dr. Smolder Bravestone]  = 1. [Ruby Roundhouse] = 2. [Professor Shelly Oberon] = 3. [Franklin Finbar] = 4.\n")
    if b == " 1":
        name="Dr.Smolder Bravestone"
       

    elif b == " 2":
        name="Ruby Roundhouse"

    elif b == " 3":
        name="Professor Shelly Oberon"

    elif b == " 4":
        name="Franklin Finbar"
   
    else:
        print("I'm very sorry, but the program did not understand your request. Please make sure you responded with a space and then the number.")
    c= input("You picked %s, correct?\n" % name) 
    if c == " Yes" or c==" yes" or c==" correct" or c==" Correct":
        print("Okay, %s, here we go!\n" % name)
        d=input("%s, you approach level 1. There is a lead pipe on the ground, and there is an enemy agent approaching. What do you do? " % name)
        item="lead pipe"
        if d==" take" or d==" Take":
            take(item)
            e=input("Now that you have the pipe you should fight the enemy with it. Type fight to do so.")
            enemy="thug"
            if e==" fight" or e==" Fight":

                fight(item,enemy)
        else:
            e=input("you did not take the pipe and were ambushed by enemy agents. better luck next time!")



else:
    print("the program did not understand")
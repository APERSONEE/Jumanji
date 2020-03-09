#import pygame
import random
import functions
import time
from random import randint
#sound=pygame.mixer.Sound("jumanji.wav")





#print('Path to module:',pygame._file_)
#pygame.mixer.Sound.play(sound)
name = functions.introP()
d=input("%s, you approach level 1. There is a lead pipe on the ground, and there is an enemy agent approaching. What do you do?\n " % name)
item="lead pipe"
if d=="take" or d=="Take":
    functions.take(item)
    e=input("Now that you have the pipe you should fight the enemy with it. Type fight to do so.\n")
    enemy="thug"
    if e=="fight" or e=="Fight":

        functions.fight(item,enemy)
    else:
        print("you did not take the pipe and were ambushed by enemy agents. better luck next time!")



else:
    print("the program did not understand try taking something, or fighting.")
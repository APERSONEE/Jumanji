def introP():
    print("Welcome to Jumanji!")
    a=input("Here are your commands: [run] This lets you run away from your current location. [fight] This lets you attack any enemies you come across. [rest] this lets you sleep to regain health. [take] this lets you take an item you come across. [use] this lets you use the item you come across.  Type [Understood] if you understand.\n")
    if a == "Understood":
        b = input("good. Now choose your character. [Dr. Smolder Bravestone]  = 1. [Ruby Roundhouse] = 2. [Professor Shelly Oberon] = 3. [Franklin Finbar] = 4.\n")
    if b == "1":
        name="Dr.Smolder Bravestone"

    elif b == "2":
        name="Ruby Roundhouse"

    elif b == "3":
        name="Professor Shelly Oberon"

    elif b == "4":
        name="Franklin Finbar"
   
    else:
        print("I'm very sorry, but the program did not understand your request. Please make sure you responded with the number.")
    c= input("You picked %s, correct?\n" % name) 
    if c == "Yes" or c=="yes" or c=="correct" or c=="Correct":
        print("Okay, %s, here we go!\n" % name)
    return name


def fight(item,enemy):
    selfHealth=20
    enemyHealth=random.randint(10,20)
    while selfHealth > 0:
        while enemyHealth > 0:
            damageAmountN=random.randint(5,7)
            damageAmountH=random.randint(8,10)
            damage=random.randint(0,2)
            
            if damage==0:
                print("%s missed! The attack did no damage and the %s had time to attack back."% (name, enemy) )
                selfHealth=selfHealth-random.randint(4,7)
                healthCheck(selfHealth)
                time.sleep(2)
            elif damage==1:
                print("%s's attack hit! the attack did %d damage "%(name, damageAmountN))
                enemyHealth=enemyHealth-damageAmountN
                healthCheck(selfHealth)
                time.sleep(2)
            else:
                print("%s's attack hit a headshot! the attack did %d damage."%(name,damageAmountH))
                healthCheck(selfHealth)
                enemyHealth=enemyHealth-damageAmountH
                time.sleep(2)
        if enemyHealth <= 0:
            print("enemy died.")        

def take(item):
    print("%s picked up %s, and the item has been put in your inventory."% (name,item))

def use(item, location):
    pass

def healthCheck(selfHealth):
    
    print("your health is %d" % selfHealth)

def showInstructions():
      #print a main menu and the commands
  print('''
Jumanji
========
Commands:
  [run] - This lets you run away from your current location
  [fight] This lets you attack any enemies you come across.
  [rest] this lets you sleep to regain health.
  [take] this lets you take an item you come across.
  [use] this lets you use the item you come across.
''')

def showStatus():
      #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
   
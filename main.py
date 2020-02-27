from functions import *

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


rooms = {
	'Entrance': {
		'item': 'lead pipe',
	}
}
inventory = []
currentRoom = 'Entrance'

showInstructions()

while True:

	showStatus()

	move = ''
	while move == '':
		move = input('>')

	move = move.lower().split()

	if move[0] == 'run':
		print('You choose to run.')


	elif "item" in rooms[currentRoom] and move[0] == "take":
		#add the item to their inventory
		inventory += rooms[currentRoom]['item'].join(' ')
		#display a helpful message
		print(move[1] + ' got!')
		#delete the item from the room
		del rooms[currentRoom]['item']
	else:
		print('Does not work like that.')
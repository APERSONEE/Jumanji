from functions import *




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
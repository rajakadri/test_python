#guess the number code

import random

print('I am thinking of a number between 1 and 20')

myRand = random.randint(1,20)

#def guesses(input()):
#	print('Guess.')
#	myGuess = int(input())

for guessesTaken in range(1,7):
	try:
		print('Guess.')
		myGuess = int(input())
	except:
		myGuess > 20
		print('Pick a number between 1 and 20!!!')
		myGuess = int(input())
	if myGuess < myRand:
		print('Too low.')
	elif  myGuess > myRand:
		print('Too high.')
	else:
		break

if myGuess == myRand:
	print('Correct.')
else:
	print('The number was ' + str(myRand))




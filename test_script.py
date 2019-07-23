#This program says hello and aks for a name.
import random


#code

name = ''
print('Hello World!')
print('What is your name?')
myName = input()
while myName == name:
	print('Please input a name.')
	myName = input()
	if myName != name:
		break
print('It is good to meet you ' + myName)
print('The length of your name is: ')
print(len(myName))
#myList = []
#for i, c in enumerate(myName):
#	myList.append(c)
#	if i > len(myName) - 1:
#		break
print('Select a number between 1 and ' + str(len(myName)) + ' or type skip or type random.' )

#Can make input an int using int(), but will fix later

myChar = input().lower()

#Not skip or random
while myChar != 'skip' and myChar != 'random':
	if int(myChar) >= 1:
		if  int(myChar) <= len(myName):
			myList = []
			for i, c in enumerate(myName):
				myList.append(c)
			print('The ' + myChar + ' character in your name is :')
			print(*myList[int(myChar) -1])
			myChar = input().lower()
	else:
		print('Please enter a valid number.')
		myChar = input().lower()

#random
if myChar == 'random':
	myRandomList = []
	for i, c in enumerate(myName):
		myRandomList.append(c)
	print(*myRandomList[random.randint(0, len(myName)-1)])

print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

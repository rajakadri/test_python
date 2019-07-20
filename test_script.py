#This program says hello and aks for a name.

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
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

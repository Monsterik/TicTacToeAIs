from Game import TicTacToe_Env
from random import randint
import os
import time

env = TicTacToe_Env()

sum1 = 0
sum2 = 0

os.system('cls')
env.reset()
print('Your score: ',sum1,'| AI score: ',sum2)
time.sleep(2)

os.system('cls')
env.render()
print('Your score: ',sum1,'| AI score: ',sum2)
###


def wrong_input(action):
	if env.board[action-1] == 1 or env.board[action-1] == 2:
		return True
	else:
		return False

###
while(True):
	if env.player == 1:
		while(True):
			try:
				action = int(input("Please enter your choice: "))
			except ValueError:
				print("Sorry, I didn't understand that.")
				continue
			else:
				if action < 10 and action > 0:
					if wrong_input(action) == False:
						break
					else:
						print("Wrong input.")
				else:
					print("Sorry, I didn't understand that.")
	else:
		while(True):
			action = randint(1,9)
			time.sleep(0.1)
			if wrong_input(action) == False:
				print('AI TURN: ',action)
				time.sleep(0.1)
				break
			
	env.step(action)
	os.system('cls')
	env.render()
	print('Your score: ',sum1,'| AI score: ',sum2)
	if env.done == True:
		sum1 += env.reward1 
		sum2 += env.reward2
		
		time.sleep(2)
		os.system('cls')
		env.reset()
		print('Your score: ',sum1,'| AI score: ',sum2)
		time.sleep(2)
		os.system('cls')
		env.render()
		print('Your score: ',sum1,'| AI score: ',sum2)
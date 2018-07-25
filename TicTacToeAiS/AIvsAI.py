from Game import TicTacToe_Env
from Test import BrainDQN
import time
import os
from random import randint

env = TicTacToe_Env()

def wrong_input(action):
	if env.board[action-1] == 1 or env.board[action-1] == 2:
		return True
	else:
		return False

RL = BrainDQN(9)
env.playermode = False
sum1p = 0
sum2p = 0
sum1a = 0
sum2a = 0

os.system('cls')

for episode in range(110000):
	# initial observation
	observation = env.reset()
	RL.setPerception(observation, 0, 0)
	os.system('cls')
	env.render()
	#time.sleep(0.1)
	while(True):
		if env.player == 1:
			action = RL.getAction()
			action += 1
			
			#print('AI 1 TURN: ',action)
		else:
			while(True):
				action = randint(1,9)
				if wrong_input(action) == False:
					#print('AI 2 TURN: ',action)
					break
		
		#time.sleep(0.1)

		observation, reward1, reward2, done = env.step(action)
		RL.setPerception(observation, action, reward1)

		os.system('cls')
		env.render()

		if done:
			if env.reward1 == 1:
				sum1p += env.reward1 
			if env.reward2 == 1:
				sum2p += env.reward2
			sum1a += env.reward1
			sum2a += env.reward2
			#time.sleep(0.1)
			env.reset()
			break


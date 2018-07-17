from Game import TicTacToe_Env
from NeuralNet import DeepQNetwork
import time
import os
from random import randint

env = TicTacToe_Env()

def wrong_input(action):
	if env.board[action-1] == 1 or env.board[action-1] == 2:
		return True
	else:
		return False
def showstatus(step,sum1p,sum2p,sum1a,sum2a,epoch,wrong):
	string = 'Player 1 score:' + str(sum1p).rjust(4) + '| Player 2 score:' + str(sum2p).rjust(4)  + '\n' + 'AI 1 score:' + str(sum1a).rjust(4) + '| AI 2 score:' + str(sum2a).rjust(4) + '\n' + 'Step:' + str(step).rjust(4) + 'Epoch:' + str(epoch).rjust(4) + 'Wrong:' + str(wrong).rjust(4)
	print(string, end='', flush=True)

RL = DeepQNetwork(env.n_actions, env.n_features,
                    learning_rate=0.1,
                    reward_decay=0.9,
                    e_greedy=0.9,
                    replace_target_iter=50,
                    memory_size=2000,
					e_greedy_increment=0.01
                    # output_graph=True
                    )

env.playermode = False
sum1p = 0
sum2p = 0
sum1a = 0
sum2a = 0

os.system('cls')

for episode in range(110000):
	# initial observation
	observation = env.reset()
	os.system('cls')
	env.render()

	showstatus(RL.learn_step_counter,sum1p,sum2p,sum1a,sum2a,RL.epoch,env.wrong)

	#time.sleep(0.1)

	while(True):
		if env.player == 1:
			action = RL.choose_action(observation)
			action += 1
			
			#print('AI 1 TURN: ',action)
		else:
			while(True):
				action = randint(1,9)
				if wrong_input(action) == False:
					#print('AI 2 TURN: ',action)
					break
		
		#time.sleep(0.1)

		observation_, reward1, reward2, done = env.step(action)
		RL.store_transition(observation, action, reward1, observation_)
		RL.learn()

		# swap observation
		observation = observation_

		
		os.system('cls')
		env.render()

		showstatus(RL.learn_step_counter,sum1p,sum2p,sum1a,sum2a,RL.epoch,env.wrong)

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


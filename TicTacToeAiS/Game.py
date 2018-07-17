import numpy as np
import random
class TicTacToe_Env():
	def __init__(self):
		self.observation_space = [0,0,0,0,0,0,0,0,0]
		self.action_space = [0,0,0,0,0,0,0,0,0]
		self.reward1 = 0
		self.reward2 = 0
		self.done = False
		self.n_actions = 9
		self.n_features = 9
		self.playermode = True
		self.wrong = 0
	def step(self,action):
		self.done = False

		if self.board[action-1] == 1 or self.board[action-1] == 2: # WRONG TURN
			if self.player == 1:
				self.reward1 = -1
				self.reward2 = 0
				self.wrong += 1
			else:
				self.reward1 = 0
				self.reward2 = -1
			self.done = True
		else:
			self.board[action-1] = self.player

		if (self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[1] != 0) or \
		(self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[4] != 0) or \
		(self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[7] != 0) or \
		(self.board[6] == self.board[3] and self.board[3] == self.board[0] and self.board[3] != 0) or \
		(self.board[7] == self.board[4] and self.board[4] == self.board[1] and self.board[4] != 0) or \
		(self.board[8] == self.board[5] and self.board[5] == self.board[2] and self.board[5] != 0) or \
		(self.board[6] == self.board[4] and self.board[4] == self.board[2] and self.board[4] != 0) or \
		(self.board[8] == self.board[4] and self.board[4] == self.board[0] and self.board[4] != 0): #CHECK FOR WIN COMBINATION
			if self.player == 1:
				self.reward1 = 1
				self.reward2 = -1
			else:
				self.reward1 = -1
				self.reward2 = 1
			self.done = True
		else:
			if self.stalemate() == True:
				self.done = True
			if self.player == 1: 
				self.player = 2
			else:  
				self.player = 1

		if self.playermode == True:
			if self.reward1 == -1:
				self.reward1 = 0
			if self.reward2 == -1:
				self.reward2 = 0

		return self.board, self.reward1, self.reward2, self.done
	
	def render(self):
		print('           TIC TAC TOE           ')
		if self.reward1 == 0 and self.reward2 == 0 and self.done == False:
			print('---------------------------------')
			print('Player ', self.player, 'Your Turn!')
			self.print_board()
			print('---------------------------------')
		elif self.reward1 == 1:
			print('---------------------------------')
			print('Player 1 Wins!')
			self.print_board()
			print('---------------------------------')
		elif self.reward2 == 1:
			print('---------------------------------')
			print('Player 2 Wins!')
			self.print_board()
			print('---------------------------------')
		elif self.stalemate() == True:
			print('---------------------------------')
			print('Nobody Wins! You are fools!')
			self.print_board()
			print('---------------------------------')
		else:
			print('---------------------------------')
			print('AI WRONG TURN!')
			self.print_board()
			print('---------------------------------')

	def reset(self):
		if self.playermode == True:
			self.board = np.array([3,3,3,3,3,3,3,3,3])
			print('           TIC TAC TOE           ')
			print('---------------------------------')
			print('Restarting...')
			self.print_board()
			print('---------------------------------')
		self.board = np.array([0,0,0,0,0,0,0,0,0])
		self.player = random.randint(1,2)
		self.reward1 = 0
		self.reward2 = 0
		self.done = False
		return self.board


	####################

	def print_board(self):
		printed_board = '''
	|%s|%s|%s|
	-------
	|%s|%s|%s|
	-------
	|%s|%s|%s|
	''' % (self.board[6], self.board[7],self.board[8],self.board[3],self.board[4],self.board[5],self.board[0],self.board[1],self.board[2])
		printed_board = printed_board.replace('0', ' ')
		printed_board = printed_board.replace('1', 'X')
		printed_board = printed_board.replace('2', 'O')
		printed_board = printed_board.replace('3', '#')
		print(printed_board)
	def stalemate(self):
		if (self.board[0] != 0 and self.board[1] != 0 and self.board[2] != 0 and self.board[3] != 0 and self.board[4] != 0 and self.board[5] != 0 and self.board[6] !=0 and self.board[7] != 0 and self.board[8] != 0):
			return True
		else:
			return False
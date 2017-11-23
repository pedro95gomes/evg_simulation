from player import Player

def create_matrix(matrix_size,strategy):
	matrix=[[0 for i in range(matrix_size)] for j in range(matrix_size)]
	for i in range(matrix_size):
		for j in range(matrix_size):
			matrix[i][j]=Player(strategy)
	return matrix

class snowdrift(object):
	"""Game Type Prisoner Dillema"""
	def __init__(self, matrix_size, strategy):
		self.matrix=create_matrix(matrix_size,strategy)
		self.actionPayoffs = {
			"T":10,
			"R":7,
			"S":3,
			"P":0
		}
		self.round=0
	
	def getGameMatrix(self):
		return self.matrix

	def getRounds(self):
		return self.round

	def getActionPayoffs(self, letter):
		return self.actionPayoffs[letter]

	def setPayoff(self, player1, player2):
		if(player1.action=="C" and player2.action=="C"):
			player1.payoffs.append(self.getActionPayoffs("R"))
		elif(player1.action=="C" and player2.action=="D"):
			player1.payoffs.append(self.getActionPayoffs("S"))
		elif(player1.action=="D" and player2.action=="C"):
			player1.payoffs.append(self.getActionPayoffs("T"))
		elif(player1.action=="D" and player2.action=="D"):
			player1.payoffs.append(self.getActionPayoffs("P"))
		else:
			print("Wrong actions-Player1:" + player1.action + "-Player2:" + player2.action)
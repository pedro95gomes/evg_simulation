from prisoner_dillema import prisoner_dillema
from snowdrift import snowdrift

def create_game(matrix_size, strategy, gameType):
	if (gameType=='P'):
		return prisoner_dillema(matrix_size,strategy)
	elif (gameType=='S'):
		return snowdrift(matrix_size,strategy)
	else:
		print("Wrong game type\n")

class Game(object):
	"""Game class"""
	def __init__(self, matrix_size, strategy, gameType):
		self.type=gameType
		self.game=create_game(matrix_size,strategy,gameType)

	def getGame(self):
		return self.game
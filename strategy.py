from unconditional_imitation import Unconditional_Imitation
from replicator_rule import Replicator_Rule

def create_strategy(strategy):
	if (strategy=='UI'):
		return Unconditional_Imitation()
	elif (strategy=='RR'):
		return Replicator_Rule()
	else:
		print("Wrong strategy\n")

class Strategy(object):
	"""Class for Strategy"""
	def __init__(self, strategy):
		self.type=strategy
		self.strategy=create_strategy(strategy)

	def getStrategy(self):
		return self.strategy

	def getType(self):
		return self.type


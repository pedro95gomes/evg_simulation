from strategy import Strategy

class Player(object):
	"""Player class"""

	def __init__(self, strategy):
		self.probability=0.5
		self.payoffs=[]
		self.lastPayoff=0
		self.strategy=Strategy(strategy)
		self.action=""
		self.pastActions=[]

	def total_payoff(self):
		return sum(self.payoffs)

	def getLastPayoff(self):
		return self.lastPayoff

	def emptyPayoffs(self):
		self.payoffs=[]

	def setLastPayoff(self, payoff):
		self.lastPayoff=payoff

	def getLastAction(self):
		return self.action

	def getProbability(self):
		return self.probability

	def getPastActions(self):
		return self.pastActions

	def setAction(self,action):
		self.action=action
		self.pastActions.append(action)

	def getStrategy(self):
		return self.strategy

	def applyStrategy(self,matrix):
		action=self.strategy.apply(matrix)



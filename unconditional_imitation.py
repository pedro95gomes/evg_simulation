class Unconditional_Imitation(object):
	"""Class for strategy Unconditional Imitation"""
	def __init__(self):
		self.type="UI"

	def getNeighbours(self, matrix, position, numberNeigh):
		neigh=[]
		if(numberNeigh==8):
			neighboursPos=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
		elif(numberNeigh==4):
			neighboursPos=[[0 , 1], [1, 0], [-1, 0], [0, -1]]
		else:
			print("Wrong number of neighbours")

		for i in range(numberNeigh):
			row=position[0] + neighboursPos[i][0]
			column=position[1] + neighboursPos[i][1]
			if(row==len(matrix)):
				row=0
			if(column==len(matrix)):
				column=0
			neigh.append(matrix[row][column])

		return neigh

	def getBestNeighbour(self, neigh):
		bestN=neigh[0]
		for n in neigh:
			if(n.getLastPayoff()>bestN.getLastPayoff()):
				bestN=n
		return bestN

	def getBestAction(self, matrix, position, numberNeigh):
		neighbours=self.getNeighbours(matrix, position, numberNeigh)
		bestNeighbour=self.getBestNeighbour(neighbours)

		return bestNeighbour.getLastAction()

		
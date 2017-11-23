from __future__ import division
import random

class Replicator_Rule(object):
	"""Class for strategy Unconditional Imitation"""
	def __init__(self):
		self.type="RR"

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

	def calculateAction(self, matrix, position, numberNeigh, neighbours):
		playeri = matrix[position[0]][position[1]]
		randneighbour = neighbours[random.randint(0,numberNeigh-1)]
		playeri_payoff=playeri.getLastPayoff()
		randneighbour_payoff=randneighbour.getLastPayoff()

		probability=(1+(randneighbour_payoff-playeri_payoff)/(numberNeigh*(max([10,7,3,0])-min([10,7,3,0]))))/2
		#print(probability)
		if(probability>=0.5):
			return randneighbour.getLastAction()
		else:
			return playeri.getLastAction()

	def getBestAction(self, matrix, position, numberNeigh):
		neighbours=self.getNeighbours(matrix, position, numberNeigh)
		bestaction=self.calculateAction(matrix, position, numberNeigh, neighbours)

		return bestaction
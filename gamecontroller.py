import matplotlib.pyplot as plt
import numpy as np
import game
import random
from game import Game

def setInitialAction(matrix):
	for row in range(len(matrix)):
		for column in range(len(matrix)):
			player = matrix[row][column]
			if(random.random() < player.getProbability()):
				player.setAction("C")
			else:
				player.setAction("D")
			#print("Player: (" + str(row) + "," + str(column) + ")  Action:"+player.getLastAction())

def setStrategyAction(matrix,num_neighbours):
	for row in range(len(matrix)):
		for column in range(len(matrix)):
			player = matrix[row][column]
			strategy = player.getStrategy().getStrategy()
			position = [row,column]
			
			action=strategy.getBestAction(matrix, position, num_neighbours)
			player.setAction(action)
			#print("Player: (" + str(row) + "," + str(column) + ")  Action:"+player.getLastAction())

def attributeAction(matrix, round_num, num_neighbours):
	if(round_num==0):
		setInitialAction(matrix)
	else:
		setStrategyAction(matrix,num_neighbours)

def calculatePayoffs(game, matrix, num_neighbours):
	for row in range(len(matrix)):
		for column in range(len(matrix)):
			player = matrix[row][column]
			strategy = player.getStrategy().getStrategy()
			position=[row,column]
			neighbours = strategy.getNeighbours(matrix, position, num_neighbours)

			for neigh in neighbours:
				game.setPayoff(player, neigh)

			player.setLastPayoff(player.total_payoff())
			player.emptyPayoffs()

def getPlayersPastActions(matrix):
	total_actions=[]
	for row in range(len(matrix)):
		for column in range(len(matrix)):
			player = matrix[row][column]
			total_actions.append(player.getPastActions())
	return total_actions

def plotCooperationMatrix(matrix, round_num, info):
	w_title=info[2]+"-"+info[1]+str(info[0])+"-"+str(info[4])+"-"+str(round_num)

	matrix_cooperation=np.zeros((len(matrix),len(matrix),3))
	for row in range(len(matrix)):
		for column in range(len(matrix)):
			if(matrix[row][column].getLastAction()=="C"):
				matrix_cooperation[row][column]=[0,1,0]
			else:
				matrix_cooperation[row][column]=[1,0,0]

	plotImage(w_title, info[0]+1, matrix_cooperation)

def plotImage(w_title, round_num,matrix_cooperation):
	fig = plt.gcf()
	fig.canvas.set_window_title(w_title)
	plt.imshow(matrix_cooperation, cmap='Greys',  interpolation='nearest')
	plt.title(w_title)
	plt.xticks(np.arange(0, round_num, 5))
	plt.yticks(np.arange(0, round_num, 5))
	plt.savefig(w_title+".png")
	plt.gcf().clear()
	#plt.show()

def plotGraph(w_title, cooperation, iterations):
	fig = plt.gcf()
	fig.canvas.set_window_title(w_title)
	plt.plot(cooperation)
	plt.xticks(np.arange(0, iterations, 2))
	plt.xlabel('Rounds')
	plt.ylabel('Cooperation')
	plt.title("Cooperation over Time")
	plt.savefig(w_title+".png")
	#plt.show()

def write_to_file(w_title, r, coop, defect):
	tofile="Round:"+r+"\nC:"+coop+"\nD:"+defect+"\n"
	file=open(w_title+".txt",'a')
	file.write(tofile)
	file.close()

def plotCooperationLevels(matrix, iterations, info):
	cooperation=[]
	w_title=info[2]+"-"+info[1]+str(info[0])+"-"+str(info[4])+"-CooperationOverTime"

	playersActions=getPlayersPastActions(matrix)
	for r in range(iterations):
		cooperationdefect={"C":0,"D":0}
		for player_acts in playersActions:
			if(player_acts[r]=="C"):
				cooperationdefect["C"]+=1
			else:
				cooperationdefect["D"]+=1
		cooperation.append(cooperationdefect["C"])
		write_to_file(w_title, str(r+1), str(cooperationdefect["C"]), str(cooperationdefect["D"]))
	
	plotGraph(w_title, cooperation, iterations+1)

	return cooperation

def main():
	"""Main function"""
	"""Made by Pedro Gomes@IST"""
	#------------------------------------------------#
	"""game(matrix size, strategy type, game type)"""
	"""Matrix Size: 4x4 , 8x8 , 12x12 , 20x20 , 50x50"""
	"""Strategy Type: UI-Unconditional Imitation , RR-Replicator Rule """
	"""Game Type: P-Prisoners Dillema , S-Snowdrift"""
	matrix_size=50
	strategy_type="UI"
	game_type="P"
	"""NUMBER OF ROUNDS"""
	iterations=51
	"""NUMBER OF NEIGHBOURS"""
	num_neighbours=8
	"""FULL INFORMATION LIST"""
	info=[matrix_size,strategy_type,game_type,iterations,num_neighbours]

	game=Game(matrix_size, strategy_type, game_type)
	specific_game=game.getGame()
	matrix=specific_game.getGameMatrix()
	for round_num in range(iterations):
		attributeAction(matrix, round_num, num_neighbours)
		calculatePayoffs(specific_game, matrix, num_neighbours)
		if(round_num in (0,1,2,5,10,20,50)):
			plotCooperationMatrix(matrix, round_num, info)
	cooperation=plotCooperationLevels(matrix, iterations, info)
	return 0

main()
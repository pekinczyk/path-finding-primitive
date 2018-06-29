import random,os
clear = lambda: os.system('cls')
class Maze():
	def __init__(self,width = 16, height = 16, start_point = (1,0), show_progress = False):
		self.mx = width
		self.my = height
		self.maze = [[1 for x in range(self.mx)] for y in range(self.my)]
		self.solved_maze = None
		self.startP = start_point
		self.endP = None # end not yet definied
		self.pathArr = None
		self.solved = False
		dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
		stack = [self.startP]
		while len(stack) > 0:
			(cx, cy) = stack[-1]
			self.maze[cy][cx] = 0
			# find a new cell to add
			nlst = [] # list of available neighbors
			for i in range(4):
				nx = cx + dx[i]
				ny = cy + dy[i]
				if nx >= 1 and nx < self.mx-1 and ny >= 1 and ny < self.my-1:
					if self.maze[ny][nx] == 1:
						# of occupied neighbors must be 1
						ctr = 0
						for j in range(4):
							ex = nx + dx[j]; 
							ey = ny + dy[j]
							if ex >= 0 and ex < self.mx and ey >= 0 and ey < self.my:
								if self.maze[ey][ex] == 0: ctr += 1
						if ctr == 1: nlst.append(i)
			# if 1 or more neighbors available then randomly select one and move
			if len(nlst) > 0:
				ir = nlst[random.randint(0, len(nlst) - 1)]
				cx += dx[ir]; cy += dy[ir]
				stack.append((cx, cy))
			else: stack.pop()
			if show_progress:
				print(self)
				clear()
		
		for i in range(len(self.maze[-2])-1,0,-1):
			if self.maze[-2][i] == 0:
				self.endP = (i,self.my-1) # set exit point
				self.maze[-1][i] = 0 # break last wall
				break
	def start(self):
		return self.startP
	def end(self):
		return self.endP
	def solve(self,show_progress = False):
		
		# BEGIN !
		Grid = {}
		Node.start_n = self.startP
		Node.end_n = self.endP
		x = self.mx
		y = self.my
		
		# CREATE NODES GRID
		for yy in range(y):
			for xx in range(x):
				position = (xx,yy)
				Grid[position] = Node(xx,yy)
				Grid[position].obstacle = self.maze[yy][xx] == 1
		# INIT NEIGHBOURS
		for yy in range(y):
			for xx in range(x):
				node = Grid[(xx,yy)]
				for nx,ny in [[1,0],[-1,0],[0,1],[0,-1]]:
					try:
						node.neighbours += [Grid[(node.x+nx,node.y+ny)]]
					except:pass;

		start_node = Grid[self.startP]
		end_node = Grid[self.endP]

		wanderer = pathFinder(start_node,end_node)
		#clear()
		while wanderer.inProgress:
			wanderer.keepGoing()
			if show_progress:
				clear()
				printNodes(Grid,x,y,start_node,end_node,end_node.road)		
		p = []
		for nod in end_node.road:
			p += [(nod.x,nod.y)]
		self.pathArr = list(reversed(p))
		
		self.solved_maze = self.maze.copy()
		for (xx,yy) in self.pathArr:
			self.solved_maze[yy][xx] = 2	
		self.solved = True
		
	def __str__(self):
		s = ""
		m = self.maze
		if self.solved:
			m = self.solved_maze
		for y,row in enumerate(self.maze):
			for x,node in enumerate(row):
				if (x,y) == self.startP:
					s += "S"
				elif (x,y) == self.endP:
					s += "E"
				else:
					s += [" ","█","."][node]
			s += "\n"
		return s
	def mazeArray(self):
		return self.maze
	def path(self):
		return self.pathArr
	def solvedMazeArray(self):
		return self.solved_maze
class Node:
	start_n,end_n = (-1,-1),(-1,-1)
	def __init__(self,xx,yy):
		self.x = xx
		self.y = yy
		self.visited = False
		self.obstacle = False
		self.road = [self]
		self.neighbours = []
	def __str__(self):
		if (self.x,self.y) == self.start_n:
			return "S"
		if (self.x,self.y) == self.end_n:
			return "E"
		return ['░',' ','▒','█'][self.visited + 2*self.obstacle]
class pathFinder():
	def __init__(self,start,goal):
		self.path_table = [start]
		self.goal = goal
		self.inProgress = True
		self.maxSize = -1
		self.allIterations = 1
	def keepGoing(self):
		if not self.goal.visited:
			new_path_table = []
			for node in self.path_table:
				node.visited = True
				if not node.obstacle:
					for nb in node.neighbours:
						if not nb.visited:
							new_path_table.extend([nb])
							nb.road.extend(node.road)
			
			self.path_table = new_path_table
			size = len(self.path_table)
		else:
			self.inProgress = False
def printNodes(grid,gx,gy,s,e,nodes=[]):
	for yy in range(gy):
		for xx in range(gx):
			node = grid[(xx,yy)]
			if nodes:
				if node in nodes and not node in [s,e]:
					print(".",end="")
				else:
					print(node,end="")
			else:
				print(node,end="")
		print()

# maze-generator

Random Maze Generator (Depth-first Search) with Path Finding
I used this (http://code.activestate.com/recipes/578356-random-maze-generator/) and added interface for generating and solving the maze. 

INTERFACE:

Maze(width,height,start_point, show_progress*) - 
create maze object,
maze starts in point start_point [default=(1,0)],
maze ends somewhere in lower right part of the maze,
to print maze simply use print(maze_obj)

.mazeArray()	<-	get unsolved maze 2D-array

.start()		<-	get start point tuple (x,y)

.end()			<-	get end point tuple (x,y)

.solve(show_progress*)	<-	solve the maze, I used my old code for path finding in 2D-grid of nodes

.path()			<-	get path from start to exit**

.solvedMazeArray()	<-	get solved maze 2D-array**


( * - show_progress - optional, display algorithm progress )

( ** - only after maze is solved )

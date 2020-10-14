import queue
import math
import time
from queue import PriorityQueue
from draw_maze_function import drawMaze

# ===== Constants =====
START = "#"
END = "$"
PATH = "*"
WALL = "-"
HEURISTIC = "manhattan"
# HEURISTIC = "euclidian"

# ===== Classes =====
class Maze():               
    def __init__(self, grid, lines, columns, startI, startJ, endI, endJ):
        self.grid = grid
        self.lines = lines
        self.columns = columns
        self.startI = startI
        self.startJ = startJ
        self.endI = endI
        self.endJ = endJ

# ===== Functions =====  
def fFunction(steps, curPos, end, type):
  if (type == "manhattan"): distance = abs(curPos[0]-end[0]) + abs(curPos[1]-end[1])

  if (type == "euclidian"): distance = math.sqrt((curPos[0] - end[0])**2 + (curPos[1] - end[1])**2)
  
  # f = g + h
  return (steps + 1) + distance

def readMaze(fileName):
  f = open("../mazes/"+fileName, "r")
  firstLine = f.readline()
  mazeInfo = firstLine.split()
  lines = int(mazeInfo[0])
  columns = int(mazeInfo[1])

  maze = [[0 for x in range(columns)] for y in range(lines)] 
  for i in range (0, lines):
    fileLine = f.readline()
    for j in range (0, columns):
      maze[i][j] = fileLine[j]
      if (fileLine[j] == START):
        startI = i
        startJ = j
      if (fileLine[j] == END):
        endI = i
        endJ = j


  mazeObj = Maze(maze, lines, columns, startI, startJ, endI, endJ)
  return mazeObj

def insideGrid(i, j, lines, columns):
  if (i < 0 or i >= lines): return False
  if (j < 0 or j >= columns): return False
  return True

def A_start(grid, start, end, lines, columns):
  pq = PriorityQueue()
  path = [start]
  steps = 0
  pq.put((0, (start, [start], 0)))
  visited = set()

  while(not pq.empty()):
    weight, (node, path, steps) = pq.get()

    i = node[0]
    j = node[1]
    if ((i,j) in visited): continue

    visited.add((i,j))
    # print("Visitando: (",i,",",j,")")

    if ((i,j) == end):
      print("End found in:(", i, ",", j,")")
      return path, visited

    if (insideGrid(i,j+1,lines,columns) and grid[i][j+1] != WALL and (i,j+1) not in visited):
      newPath = path + [(i,j+1)]
      f = fFunction(steps, (i,j+1), end, HEURISTIC)
      # print("Colocando ({},{}) com peso {}".format(i, j+1, f))
      pq.put((f, ((i,j+1), newPath, steps+1)))
    if (insideGrid(i+1,j,lines,columns) and grid[i+1][j] != WALL and (i+1,j) not in visited):
      newPath = path + [(i+1,j)]
      f = fFunction(steps, (i+1,j), end, HEURISTIC)
      # print("Colocando ({},{}) com peso {}".format(i+1, j, f))
      pq.put((f, ((i+1,j), newPath, steps+1)))
    if (insideGrid(i,j-1,lines,columns) and grid[i][j-1] != WALL and (i,j-1) not in visited):
      newPath = path + [(i,j-1)]
      f = fFunction(steps, (i,j-1), end, HEURISTIC)
      # print("Colocando ({},{}) com peso {}".format(i, j-1, f))
      pq.put((f, ((i,j-1), newPath, steps+1)))
    if (insideGrid(i-1,j,lines,columns) and grid[i-1][j] != WALL and (i-1,j) not in visited):
      newPath = path + [(i-1,j)]
      f = fFunction(steps, (i-1,j), end, HEURISTIC)
      # print("Colocando ({},{}) com peso {}".format(i-1, j, f))
      pq.put((f, ((i-1,j), newPath, steps+1)))


def main():
  start_time = time.time()*1000
  maze = readMaze("maze7.txt")
  path, visited = A_start(maze.grid, (maze.startI, maze.startJ), (maze.endI, maze.endJ), maze.lines, maze.columns)
  print("Path:", path)
  milliseconds = time.time()*1000 - start_time
  print("Execution time:", milliseconds, "ms")
  drawMaze(maze.grid, maze.lines, maze.columns, path, visited)

if __name__ == "__main__": main()
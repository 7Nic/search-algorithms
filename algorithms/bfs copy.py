import queue

# ===== Constants =====
START = "#"
END = "$"
PATH = "*"
WALL = "-"

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
      # print("Vendo", i, j, fileLine[j])
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

def bfs(grid, start, end, lines, columns):
  q = queue.Queue() 
  q.put(start)

  visited = set()

  while(not q.empty()):
    i, j = q.get()

    if ((i,j) in visited): continue

    visited.add((i,j))
    print("Visitando: (",i,",",j,")")

    if ((i,j) == end):
      print("Achamos a saída em ", i, j)
      return

    if (insideGrid(i,j+1,lines,columns) and grid[i][j+1] != WALL and (i,j+1) not in visited):
      q.put((i,j+1))
    if (insideGrid(i,j-1,lines,columns) and grid[i][j-1] != WALL and (i,j-1) not in visited):
      q.put((i,j-1))
    if (insideGrid(i+1,j,lines,columns) and grid[i+1][j] != WALL and (i+1,j) not in visited):
      q.put((i+1,j))
    if (insideGrid(i-1,j,lines,columns) and grid[i-1][j] != WALL and (i-1,j) not in visited):
      q.put((i-1,j))

def main():
  maze = readMaze("maze2.txt")
  bfs(maze.grid, (maze.startI, maze.startJ), (maze.endI, maze.endJ), maze.lines, maze.columns)


if __name__ == "__main__": main()
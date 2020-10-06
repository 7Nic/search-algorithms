class Maze():               
    def __init__(self, grid, lines, columns, startI, startJ, endI, endJ):
        self.grid = grid
        self.lines = lines
        self.columns = columns
        self.startI = startI
        self.startJ = startJ
        self.endI = endI
        self.endJ = endJ

def readMaze():
  f = open("../mazes/maze1.txt", "r")
  firstLine = f.readline()
  mazeInfo = firstLine.split()
  lines = int(mazeInfo[0])
  columns = int(mazeInfo[1])

  maze = [[0 for x in range(columns)] for y in range(lines)] 
  for i in range (0, lines):
    fileLine = f.readline()
    for j in range (0, columns):
      maze[i][j] = fileLine[j]
      if (fileLine[j] == "#"):
        startI = i
        startJ = j
      if (fileLine[j] == "$"):
        endI = i
        endJ = j

  mazeObj = Maze(maze, lines, columns, startI, startJ, endI, endJ)
  return mazeObj

def main():
  maze = readMaze()
  print(maze.lines)




if __name__ == "__main__": main()
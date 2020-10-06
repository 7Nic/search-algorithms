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

  return (maze, lines, columns)


def main():
  maze, lines, columns = readMaze()
  print(maze[0][0])

  


if __name__ == "__main__": main()
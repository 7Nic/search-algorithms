
def main():
  f = open("../mazes/maze1.txt", "r")
  mazeInfo = f.readline().split()
  width = int(mazeInfo[0])
  height = int(mazeInfo[1])
  maze = [[0 for x in range(width)] for y in range(height)] 
  
  for i in range (0, width):
    fileLine = f.readline()
    for j in range (0, height):
      maze[i][j] = fileLine[j]

  print(maze[9][9])

  


if __name__ == "__main__": main()
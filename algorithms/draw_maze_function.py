import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

# ===== Constants =====
START = "#"
END = "$"
PATH = "*"
WALL = "-"
WALL_VALUE = 3
EMPTY_PATH_VALUE = 7
START_VALUE = 13
END_VALUE = 17
PATH_VALUE = 23
VISITED_VALUE = 27

# ===== Function =====
def drawMaze(maze, lines, columns, path, visited):
  # Convert chars to numbers
  for i in range(0,lines):
    for j in range(0,columns):
      if ((i,j) in visited):
        maze[i][j] = VISITED_VALUE
      elif (maze[i][j] == WALL): 
        maze[i][j] = WALL_VALUE
      elif (maze[i][j] == PATH): 
        maze[i][j] = EMPTY_PATH_VALUE
      elif (maze[i][j] == START): 
        maze[i][j] = START_VALUE
      elif (maze[i][j] == END): 
        maze[i][j] = END_VALUE
      


  for pos in path:
    if (maze[pos[0]][pos[1]] != START_VALUE and maze[pos[0]][pos[1]] != END_VALUE): maze[pos[0]][pos[1]] = PATH_VALUE
    

  # create discrete colormap
  cmap = colors.ListedColormap(['black', 'white', 'blue',  'red', 'green', 'yellow'])
  bounds = [0, 5, 10, 15, 20, 25, 30]
  norm = colors.BoundaryNorm(bounds, cmap.N)

  fig, ax = plt.subplots()
  ax.imshow(maze, cmap=cmap, norm=norm)

  # draw gridlines
  # ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
  # ax.set_xticks(np.arange(0, SIZE, 1));
  # ax.set_yticks(np.arange(0, SIZE, 1));

  plt.show()
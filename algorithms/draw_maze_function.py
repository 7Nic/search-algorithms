import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

# ===== Constants =====
START = "#"
END = "$"
PATH = "*"
WALL = "-"

# ===== Function =====
def drawMaze(maze, lines, columns, path):
  # Convert chars to numbers
  for i in range(0,lines):
    for j in range(0,columns):
      if (maze[i][j] == WALL): maze[i][j] = 3
      if (maze[i][j] == PATH): maze[i][j] = 7
      if (maze[i][j] == START): maze[i][j] = 13
      if (maze[i][j] == END): maze[i][j] = 17


  for pos in path:
    if (maze[pos[0]][pos[1]] != 13 and maze[pos[0]][pos[1]] != 17): maze[pos[0]][pos[1]] = 23
    

  # create discrete colormap
  cmap = colors.ListedColormap(['black', 'white', 'blue',  'red', 'yellow'])
  bounds = [0, 5, 10, 15, 20, 25]
  norm = colors.BoundaryNorm(bounds, cmap.N)

  fig, ax = plt.subplots()
  ax.imshow(maze, cmap=cmap, norm=norm)

  # draw gridlines
  # ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
  # ax.set_xticks(np.arange(0, SIZE, 1));
  # ax.set_yticks(np.arange(0, SIZE, 1));

  plt.show()
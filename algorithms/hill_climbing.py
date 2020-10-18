from draw_maze_function import drawMaze
import time

# ===== Constants =====
START = "#"
END = "$"
PATH = "*"
WALL = "-"

def readMaze():
  f = open("../mazes/maze1.txt", "r")
  firstLine = f.readline()
  mazeInfo = firstLine.split()
  lines = int(mazeInfo[0])
  columns = int(mazeInfo[1])
  start = None
  end = None
  
  maze = [[0 for x in range(columns)] for y in range(lines)] 
  for i in range (0, lines):
    fileLine = f.readline()
    for j in range (0, columns):
      maze[i][j] = fileLine[j]
      if (maze[i][j] == START):
        start = (i,j)
      if (maze[i][j] == END):
        end = (i,j)


  return (maze, lines, columns, start, end)

def distance(current_pos, goal_pos):
  return abs(goal_pos[0] - current_pos[0]) + abs(goal_pos[1] - current_pos[1])

def is_valid(maze,lines, columns,pos):
  return pos[0] >= 0 and pos[1] >= 0 and pos[0] < lines and pos[1] < columns and maze[pos[0]][pos[1]] != WALL

def hill_climbing(maze, lines, columns, start, end):
  directions = ((0,1), (1,0), (-1, 0), (1, 0))
  path = [start]
  current_pos = start
  current_dist = distance(current_pos, end)
  found_path = True
  
  
  while (current_pos != end):
    next_pos = None
    next_dist = current_dist
    moved = False
    for direction in directions:
      next_pos = (direction[0] + current_pos[0], direction[1] + current_pos[1])
      next_dist = distance(next_pos, end)
      if (is_valid(maze, lines, columns, next_pos) and next_dist < current_dist):
        current_pos = next_pos
        current_dist = next_dist
        path.append(next_pos)
        moved = True
        break
    if not moved:
      break
  
  found_path = current_pos == end
  return (path, found_path)



def main():
  start_time = time.time()*1000
  maze, lines, columns, start, end = readMaze()
  path, found_path = hill_climbing(maze, lines, columns, start, end)
  visited = path
  milliseconds = time.time()*1000 - start_time
  print("Path: ", path)
  print("Execution time:", milliseconds, "ms")
  drawMaze(maze, lines, columns, path, visited)
  
  

if __name__ == "__main__": main()
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

SIZE = 300

data = np.random.rand(SIZE, SIZE) * 20
# data = [[1, 4, 5], 
#     [-5, 8, 9],
#     [12, 17, 23]]

# create discrete colormap
cmap = colors.ListedColormap(['red', 'blue', 'green',  'black'])
bounds = [0, 5, 10, 15, 20]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap, norm=norm)

# draw gridlines
# ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
# ax.set_xticks(np.arange(0, SIZE, 1));
# ax.set_yticks(np.arange(0, SIZE, 1));

plt.show()
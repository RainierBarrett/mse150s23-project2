import os
import numpy as np
import matplotlib.pyplot as plt

data_dir = 'raw_data'
save_dir = 'Average_height_plot'

methods = ['Method 1', 'Method 2', 'Method 3', 'Method A', 'Method B', 'Method C', 'method 1', 'method 2', 'method 3', 'method A', 'method B', 'method C']
colors = ['red', 'green', 'blue', 'black', 'yellow', 'purple', 'red', 'green', 'blue', 'black', 'yellow', 'purple']

for filename in os.listdir(data_dir):
    with open(os.path.join(data_dir, filename), 'r') as f:
        rows = f.readlines()
        if len(rows) < 6:
            continue
        method = rows[5].split(': ')[1].strip()
    
    if method in methods:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        avg_heights = np.mean(data, axis=0)
        
        plt.plot(avg_heights, color=colors[methods.index(method)])
        plt.title(method)
        plt.xlabel("Position")
        plt.ylabel("Height (nm)")
        plt.savefig(os.path.join(save_dir, method + ".png"))
        plt.show()


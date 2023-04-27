import os
import numpy as np
import matplotlib.pyplot as plt

data_dir = 'raw_data'

methods = ['method 1', 'method 2', 'method 3', 'method A', 'method B', 'method C']
colors = ['red', 'green', 'blue', 'black', 'yellow', 'purple']

for filename in os.listdir(data_dir):
    with open(os.path.join(data_dir, filename), 'r') as f:
        rows = f.readlines()
        method = rows[5].split(': ')[1].strip()
    
    if method in methods:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        
        plt.imshow(data, cmap='viridis')
        plt.colorbar()
        plt.title(method)
        plt.show()


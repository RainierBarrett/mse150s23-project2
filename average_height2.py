import os
import numpy as np
import matplotlib.pyplot as plt

data_dir = 'raw_data'

methods = ['method 1', 'Method 1', 'method 2', 'Method 2', 'method 3', 'Method 3', 'method A', 'Method A', 'method B', 'Method B', 'method C', 'Method C']

method1_data = []
method2_data = []
method3_data = []

for filename in os.listdir(data_dir):
    with open(os.path.join(data_dir, filename), 'r') as f:
        rows = f.readlines()
        method = rows[5].split(': ')[1].strip()

    if method in ['method 1', 'method A', 'Method A', 'Method 1']:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        method1_data.append(data)
    elif method in ['method 2', 'Method 2', 'method B', 'Method B']:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        method2_data.append(data)
    elif method in ['method 3', 'Method 3', 'method C', 'Method C']:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        method3_data.append(data)

method1 = np.asarray(method1_data)
method2 = np.asarray(method2_data)
method3 = np.asarray(method3_data)

average_height2 = np.mean(method2, axis=0)
average_height3 = np.mean(method3, axis=0)
average_height1 = np.mean(method1, axis=0)
plt.imshow(average_height1)
plt.title('Method 1 (nm)')
plt.colorbar()
plt.show()
plt.imshow(average_height2)
plt.title('Method 2 (nm)')
plt.colorbar()
plt.show()
plt.imshow(average_height3)
plt.title('Method 3 (nm)')
plt.colorbar()
plt.show()



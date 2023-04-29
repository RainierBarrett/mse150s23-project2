import os
import numpy as np

data_dir = 'raw_data'

methods = ['method 1', 'Method 1', 'method 2', 'Method 2', 'method 3', 'Method 3', 'method A', 'Method A', 'method B', 'Method B', 'method C', 'Method C']

method1_data = []
method2_data = []
method3_data = []
methodA_data = []
methodB_data = []
methodC_data = []

for filename in os.listdir(data_dir):
    with open(os.path.join(data_dir, filename), 'r') as f:
        rows = f.readlines()
        method = rows[5].split(': ')[1].strip()

    if method in ['method 1', 'Method 1']:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        method1_data.append(data)
    elif method in ['method 2', 'Method 2']:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        method2_data.append(data)
    elif method in ['method 3', 'Method 3']:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        method3_data.append(data)
    elif method in ['method A', 'Method A']:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        methodA_data.append(data)
    elif method in ['method B', 'Method B']:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        methodB_data.append(data)
    elif method in ['method C', 'Method C']:
        data = np.loadtxt(os.path.join(data_dir, filename), skiprows=6)
        methodC_data.append(data)

method1_stdev = np.std(method1_data)
method2_stdev = np.std(method2_data)
method3_stdev = np.std(method3_data)
methodA_stdev = np.std(methodA_data)
methodB_stdev = np.std(methodB_data)
methodC_stdev = np.std(methodC_data)

print(f"Method 1 stdev: {method1_stdev}")
print(f"Method 2 stdev: {method2_stdev}")
print(f"Method 3 stdev: {method3_stdev}")
print(f"Method A stdev: {methodA_stdev}")
print(f"Method B stdev: {methodB_stdev}")
print(f"Method C stdev: {methodC_stdev}")


import numpy as np
import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]

data = np.loadtxt(filename, delimiter=' ')


count=0
f = open(filename, 'r')
for line in f:
	count+=1
	if count == 6:
		method_type = line.split()[3]
		print('method is',method_type)

plt.imshow(data)
plt.title('Sample ' + filename[9:12]+' Where Method is '+str(method_type))
plt.savefig('test-image'+filename[9:12]+'.png')
plt.show()

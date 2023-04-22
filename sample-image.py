import numpy as np
import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]

data = np.loadtxt(filename, delimiter=' ')


plt.imshow(data)
plt.title('Sample ' + filename[9:12])
plt.savefig('test-image'+filename[9:12]+'.png')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import sys

filenames = sys.argv[1:]

for filename in filenames:
	data = np.loadtxt(filename, delimiter=' ')


	count=0
	f = open(filename, 'r')
	for line in f:
		count+=1
		if count == 6:
			method_type = line.split()[3]
			print('method is',method_type)

	try :
		plt.savefig('images/'+str(method_type)+'/'+filename[9:12]+'.png')
	except :
		print('Error: File save location not found, Method type '+str(method_type)+' is not an available folder')
	else:

		plt.imshow(data)
		plt.title('Sample ' + filename[9:12]+' Where Method is '+str(method_type))
		plt.savefig('images/'+str(method_type)+'/'+filename[9:12]+'.png')
		plt.show()

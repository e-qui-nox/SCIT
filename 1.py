import numpy as np 
import matplotlib.pyplot as plt
for i in range(3):
	s = np.random.poisson(10,1000)
	print(s);
	count, bins, ignored = plt.hist(s,bins=30, normed=True, color='#607c8e')
	plt.grid(axis='y', alpha=0.75)
	plt.xlabel('Value')
	plt.ylabel('Poisson Distribution')
	plt.title('Histogram')
	plt.show()
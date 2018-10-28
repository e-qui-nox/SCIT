import numpy as np 
import matplotlib.pyplot as plt
for i in range(3):
	mu,sigma=0,0.1
	s = np.random.normal(mu,sigma,1000)
	count, bins, ignored = plt.hist(s,bins=30, normed=True, color='#cd5c5c')
	plt.grid(axis='y', alpha=0.75)
	plt.xlabel('Value')
	plt.ylabel('Normal Distribution')
	plt.title('Histogram')
	plt.show()
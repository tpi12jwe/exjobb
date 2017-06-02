# pytest.py

import numpy as np
import scipy.signal as ssignal
import matplotlib.pyplot as plt



num_iter = 1

N = 4
r = 0.5
x = np.zeros([10,])
x[0] = 1

C_arr = [(np.random.randint(0,2,[N,])*2 - 1) for i in range(num_iter)]


y_arr = [ssignal.lfilter(C,1,x) for C in C_arr]

for y,C in zip(y_arr,C_arr):
	plt.figure()
	plt.title(str(C))
	plt.plot(y)

plt.show()
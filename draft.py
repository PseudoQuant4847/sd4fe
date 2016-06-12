# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# plotting simple-vs-log returns
# ============================================
x = np.linspace(-0.2, 0.2, num=10000)
y = np.log(1+x)

plt.plot(x, x, 'b-', label = 'x')
plt.plot(x, y, 'r-', label = 'log(1+x)')
plt.xlim(xmin=-0.2, xmax=0.2)
plt.ylim(ymin=-0.2, ymax=0.2)
plt.legend(loc='lower right')
plt.title('Comparison of functions log(1+x) and x.')
plt.savefig('simple-vs-log-return.jpg')
plt.close()



# plotting confidence interval of a random walk
# ============================================
mu = 0.5
sigma = 1
s0 = 0
t = np.linspace(0, 10, 1000)
mean = s0 + mu * t
mean_plus_sd = mean + sigma * (t ** 0.5)
mean_minus_sd = mean - sigma * (t ** 0.5)

plt.plot(t, mean, 'r-', label = 'mean')
plt.plot(t, mean_minus_sd, 'b-', label='mean - SD')
plt.plot(t, mean_plus_sd, 'b-', label='mean + SD')
plt.xlim(xmin=0, xmax=10)
plt.ylim(ymin=-1, ymax=9)
plt.xlabel('time')
plt.legend(loc='best')
plt.title('random walk')
plt.savefig('random_walk_range.jpg')
plt.close()
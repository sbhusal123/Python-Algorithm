import numpy as np

mean = [1, 3]
cov = [[8, -5], [0.2, 0.2]]
x = np.random.multivariate_normal([0, 2], cov, 100)

print(x)
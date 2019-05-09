import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from scipy.stats import multivariate_normal

x, y = np.mgrid[-1.0:1.0:30j, -1.0:1.0:30j]
x2, y2 = np.mgrid[-1.0:1.0:30j, -1.0:1.0:30j]

# Need an (N, 2) array of (x, y) pairs.
xy = np.column_stack([x.flat, y.flat])
xy2 = np.column_stack([x2.flat, y2.flat])

mu = np.array([0.0, 0.0])
mu2 = np.array([0.0, 1.0])

sigma = np.array([.5, .5])
covariance = np.diag(sigma**2)

sigma2 = np.array([.5, .5])
covariance2 = np.diag(sigma**2)

z = multivariate_normal.pdf(xy, mean=mu, cov=covariance)
z2 = multivariate_normal.pdf(xy2, mean=mu2, cov=covariance)

# Reshape back to a (30, 30) grid.
z = z.reshape(x.shape)
z2 = z2.reshape(x2.shape)





fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')



ax.plot_surface(x,y,z)
ax.plot_surface(x2,y2,z2)
ax.set_xlabel('PC 1')
ax.set_ylabel('PC 2')
ax.set_zlabel('PC 3')
#ax.plot_wireframe(x,y,z)

plt.show()

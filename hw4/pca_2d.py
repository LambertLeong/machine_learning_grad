# import for colormaps
import numpy as np 
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import cm

x=np.linspace(-10,10, num=100)
x2=np.linspace(0,20, num=100)
Y=np.linspace(-10,10, num=100)

x, y = np.meshgrid(x, Y)
x2, y = np.meshgrid(x2, Y)

z= np.exp(-0.1*x**2-0.1*y**2)
z2 = np.exp(-0.1*x2**2-0.1*y**2)

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot_surface(x,y,z, cmap=cm.jet)
#plt.show()

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
#ax = Axes3D(fig)
ax.scatter(x,y,z, c='r', label='pclass 0')
ax.scatter(x2,y,z2, c='b', label='pclass 0')
ax.set_xlabel('x', fontsize=30, rotation = 0)
ax.set_ylabel('y', fontsize=30, rotation = 0)
ax.set_zlabel('z', fontsize=30, rotation = 0)
#ax.scatter(x,y,z c='b', label = 'pclass 1')
plt.legend()
ax.view_init(90, 180+90)
plt.show()


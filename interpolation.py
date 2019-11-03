import numpy as np
import pdb
def func(x, y):
    return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2
# grid_x, grid_y = np.mgrid[0:1:100j, 0:1:200j]
# grid_x, grid_y = np.mgrid[0:1:100j, 0:1:100j]
grid_x, grid_y = np.mgrid[1:2:100j, 0:1:100j]

# points = np.random.rand(100, 2)
points = np.column_stack([np.random.uniform(1, 2, 1000), np.random.uniform(0, 1, 1000)])
# values = func(points[:,0], points[:,1])
values = func(points[:,0], points[:,1])

from scipy.interpolate import griddata
grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')

import matplotlib.pyplot as plt
plt.subplot(221)
plt.imshow(func(grid_x, grid_y).T, extent=(0,1,0,1), origin='lower')
plt.plot(points[:,0], points[:,1], 'k.', ms=1)
plt.title('Original')
plt.subplot(222)
plt.imshow(grid_z0.T, extent=(0,1,0,1), origin='lower')
plt.title('Nearest')
plt.subplot(223)
plt.imshow(grid_z1.T, extent=(0,1,0,1), origin='lower')
plt.title('Linear')
plt.subplot(224)
plt.imshow(grid_z2.T, extent=(0,1,0,1), origin='lower')
plt.title('Cubic')
plt.gcf().set_size_inches(6, 6)
pdb.set_trace()
plt.show()



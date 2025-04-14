
from mpl_toolkits import mplot3d

#  matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#
df = pd.read_csv('03_54_datapara3D.csv', delimiter=',')

df.columns=['x','y','z']
x = df['x']
y = df['y']
z = df['z']

#
fig = plt.figure(figsize=(10, 10), dpi=100)
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z, c='red', marker='o', edgecolors='k', s=100);
#ax.scatter3D(x2, y2, z2, c='green', marker='o', edgecolors='k');
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(0, 0)
plt.draw()
plt.pause(36000)

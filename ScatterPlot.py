from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [1,2,3,4,5,6,7,8,9,10]
Y = [5,6,13,6,17,12,1,9,10,11]
Z = [4,6,2,12,4,3,6,8,4,2]

ax.scatter(X, Y, Z, c='r', marker='o')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()
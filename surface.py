import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random


def plotSurface(fun,x,y,c):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	X, Y = np.meshgrid(x, y)
	zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
	Z = zs.reshape(X.shape)

	ax.plot_surface(X, Y, Z,color=c,rstride=1,cstride=1)

	ax.set_xlabel('ms')
	ax.set_ylabel('k')
	ax.set_zlabel('ratio')

	ax.plot_surface(X, Y, 16,color='r')


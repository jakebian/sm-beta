import matplotlib as mpl
from matplotlib import pyplot
import numpy as np

from Veff import *

# make values from -5 to 5, for this example
# make a color map of fixed colors
def plot(coords,x,y):
	cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',
	                                           ['blue','black','orange'],
	                                           256)

	bounds=[-1e2,-1e-2,1e-2,1e2]
	norm = mpl.colors.BoundaryNorm(bounds, cmap2.N)

	img2 = pyplot.imshow(coords,interpolation='nearest',
	                    cmap = cmap2,
	                    origin='lower',norm=norm)

	pyplot.colorbar(img2,cmap=cmap2)
	pyplot.xticks(np.arange(len(x)),x)
	pyplot.yticks(np.arange(len(y)),y)

	pyplot.show()

l1=0.1
res=50
k=np.linspace(0.22413,0.22667, res) 
ms=map(lambda x:x*(10**3),np.linspace(1,1.2, res))

def getPoints(fun,x,y):
	X, Y = np.meshgrid(x, y)
	zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
	Z = zs.reshape(X.shape)

	return Z
f = open('contours', 'w')
def func(ms1, k1):
  print ms1
  print k1
  # return 2
  V1=getVeff(ms1,l1,k1)
  graph1=map(lambda x: V1(x)/(x**4), dom)
  r= getRatio(graph1)-16
  st= str(k1)+"	"+str(ms1)+"	"+ str(r) + '\n'
  print st

  f.write(st)
  return r

pts= getPoints(func,ms,k)
plot(pts,ms ,k)
f.close()

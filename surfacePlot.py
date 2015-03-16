from Veff import *
from surface import *


l1=0.5

res = 3
k=np.linspace(0.4,0.6, res) 
ms=map(lambda x:x*(10**11),np.linspace(1,9, res))


# # print k


def func(ms1, k1):
  V1=getVeff(ms1,l1,k1)
  graph1=map(lambda x: V1(x)/(x**4), dom)
  r= getRatio(graph1)
  print str(ms1)+"	"+ str(k1)+"	"+r
  return r

def testFunc(a,b):
	return np.sin(a*b)
def flat(a,b):
	return 16

def flat2(a,b):
	return 1


plotSurface(func,ms,k,'b')
plt.show()
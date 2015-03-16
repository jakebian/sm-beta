from Veff import *
l0=0.1

k=0.20
ms=1e3

d= np.arange(3,18, 0.01)

dom=map(lambda x: 10**x,d)


Vpp=getVeff(ms,l0,k)[2]


graph1=map(lambda x: Vpp(x), dom)
print getZeros(graph1,d,Vpp)

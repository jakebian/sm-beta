from scipy.integrate import odeint
from beta import *
from matplotlib.pyplot import *
from scipy.interpolate import interp1d

#initial values
g1=0.46150381446263938
g2=0.64817247909999998


g3= 1.1671464903500002

lam=0.12476792090000001

yt=0.92904587628540591
yb=2.41235357077694730e-2
ytau=1.02065530839777034e-2


def getDom(d):
	return map(lambda x:x*2.30258509299*2,d)

def getGraphs(x0,d,ms):
	y = odeint(lambda x,t:getBeta(x,t,ms), x0, getDom(d))
	yp= map(lambda x: getBeta(x[0],x[1],ms),zip(y,getDom(d)))

	# plot(d,map(lambda x:x[4],yp),'r-')
	# plot(d,map(lambda x:x[5],yp),'g--')
	# plot(d,map(lambda x:x[6],yp),'b--')
	# plot(d,map(lambda x:x[7],yp),'m--')

	show()
	return [y,yp]

def interp(y,d):
	return interp1d(d,y)

def getCouplings(x0,d,ms0):
	graph=getGraphs(x0,d,ms0)
	return [getInterps(graph[0],d)+[ms0],getInterps(graph[1],d)+[0]]


def getInterps(graph,d):
	# print graph
	# print d
	g_1At=interp(map(lambda x:x[0],graph),d)
	g_2At=interp(map(lambda x:x[1],graph),d)
	g_3At=interp(map(lambda x:x[2],graph),d)

	lamAt=interp(map(lambda x:x[3],graph),d)

	y_tAt=interp(map(lambda x:x[4],graph),d)
	y_bAt=interp(map(lambda x:x[5],graph),d)
	y_tauAt=interp(map(lambda x:x[6],graph),d)

	m2At=interp(map(lambda x:x[7],graph),d)
	lam_SAt=interp(map(lambda x:x[8],graph),d)
	k_At=interp(map(lambda x:x[9],graph),d)
	
	yN_At=interp(map(lambda x:x[10],graph),d)
	
	plot(d,g_1At(d),"k.")
	plot(d,g_2At(d),"b--")
	plot(d,g_3At(d),"r--")
	plot(d,y_tAt(d),"r-")
	plot(d,lamAt(d),"k-")
	plot(d,y_bAt(d),"b-")
	plot(d,y_tauAt(d),"g-")
	plot(d,lam_SAt(d),"r.")
	plot(d,k_At(d),"b.")
	plot(d,yN_At(d),"g.")
	# plot(d,m2At(d),"k-")

	plot(d,map(lambda x: 0,d),'k--')

	show()


	return [g_1At,g_2At,g_3At,lamAt,y_tAt,y_bAt,y_tauAt,m2At,lam_SAt,k_At,yN_At]


def plotParams():
	plot(d,g_1At(d),"g--")
	plot(d,g_2At(d),"b--")
	plot(d,g_3At(d),"r--")
	plot(d,y_tAt(d),"r-")
	plot(d,lamAt(d),"k-")
	plot(d,y_bAt(d),"b-")
	plot(d,y_tauAt(d),"g-")
	plot(d,lam_SAt(d),"r.")
	plot(d,k_At(d),"b.")
	plot(d,lamAt(d),"k-")
	plot(d,map(lambda x: 0,d),'k--')
	show()

# plotParams()
from potential import *
from fitting import *
from scipy.misc import derivative
import scipy.optimize

def getZeros(list,do,func):
	zeros=[]
	def checkZero(x1,x2):
		if x1*x2<=0:
			p1=do[list.index(x1)]
			p2=do[list.index(x2)]
			zero=scipy.optimize.brentq(func,10**p1,10**p2)
			print "NEW ZERO:"+str(zero)
			zeros.append(zero)
		return x2
	reduce(checkZero, list,1)
	return zeros

def getVeff(ms0,lam_S,k,yN):
	mu=ms0
	t=ln(mu)/ln(10)

	d0 =np.arange(ln(Mt)/ln(10),19, 0.01)
	x0=[g1,g2,g3,lam,yt,yb,ytau,Mh**2,0,0,0]
	# test=[g1,g2,g3,lam,yt,yb,ytau,Mh**2,0.4,0.1]

	c00=getCouplings(x0,d0,1)
	c0=c00[0]

	V0=getV(c0)
	Vp0=getVp(c00)
	Vpp0=getVp(c00)
	d1 = np.arange(t,19, 0.01)
	# V0mu=Vfunc(c0[7](t),c0[3](t),mu)

	# Vpmu=Vp(map(lambda x:float(x(t)),c0[0:-1]),mu,0)
	# def matchV(ml):
	# 	Vnew=Vfunc(ml[0],ml[1],mu)
	# 	return -V0mu+Vnew
	# def matchVp(ml):
	# 	xsol=[g1,g2,g3,ml[1],yt,yb,ytau,ml[0],lam_S,k,yN]
	# 	Vpnew=Vp(xsol,mu,mu)
	# 	return -Vpmu+Vpnew

	# def match(ml):
	# 	return [matchV(ml),matchVp(ml)]


	newm=c0[7](t)
	newl=c0[3](t)

	def getNewParams(c0,mu):
		g1=c0[0](t)
		g2=c0[1](t)
		g3=c0[2](t)
		yt=c0[4](t)
		yb=c0[5](t)
		ytau=c0[6](t)

		lam0=c0[3](t)
		m20=c0[7](t)
		Pi=pi
		Sqrt=sqrt

		lamp0=c00[1][3](t)/mu
		newm=((-3*g1**2*mu**2)/80. - (3*g2**2*mu**2)/16. + (3*lam0*mu**2)/2. + (8*mu**2*Pi**2)/3. + (mu**2*yb**2)/4. + (mu**2*yt**2)/4. + (mu**2*ytau**2)/12. + (mu**2*Sqrt((-180*g1**2 - 900*g2**2 + 2400*lam0 + 12800*Pi**2 + 1200*yb**2 + 1200*yt**2 + 400*ytau**2)**2 - 9600*(27*g1**4 + 90*g1**2*g2**2 + 225*g2**4 - 180*g1**2*lam0 - 900*g2**2*lam0 + 3200*k**2*Pi**2 - 12800*lam0*Pi**2 - 6400*lamp0*mu*Pi**2 + 1200*lam0*yb**2 - 1200*yb**4 + 1200*lam0*yt**2 - 1200*yt**4 + 400*lam0*ytau**2 - 400*ytau**4)))/4800.)/2.
		newl=(180*g1**2 + 900*g2**2 - 2400*lam0 - 12800*Pi**2 - 1200*yb**2 - 1200*yt**2 - 400*ytau**2 - Sqrt((-180*g1**2 - 900*g2**2 + 2400*lam0 + 12800*Pi**2 + 1200*yb**2 + 1200*yt**2 + 400*ytau**2)**2 - 9600*(27*g1**4 + 90*g1**2*g2**2 + 225*g2**4 - 180*g1**2*lam0 - 900*g2**2*lam0 + 3200*k**2*Pi**2 - 12800*lam0*Pi**2 - 6400*lamp0*mu*Pi**2 + 1200*lam0*yb**2 - 1200*yb**4 + 1200*lam0*yt**2 - 1200*yt**4 + 400*lam0*ytau**2 - 400*ytau**4)))/4800.
		return newm,newl
	
	
	# try:
	# 	result = scipy.optimize.newton_krylov(match,[newm,newl] , f_tol=0.1,maxiter=int(1e5))
	# except ValueError:
	# 	print "ERROR!"
	# 	def fail(h):return False
	# 	return fail

	def match(m12,lam1,tol):
		lam2=lam1
		m22=m12
		ms=mS=ms0
		beta1=getBeta([c0[0](t),c0[1](t),c0[2](t),newl,c0[4](t),c0[5](t),c0[6](t),newm,0,0,0],ms,ms)[3]
		beta2=getBeta([c0[0](t),c0[1](t),c0[2](t),lam1,c0[4](t),c0[5](t),c0[6](t),m22,lam_S,k,yN],ms,ms)[3]
		
		for i in range(0,10):
		   m22 = m12 + mS**2*(beta1-beta2)/2
		   print m22
		   lam2 = lam1 + (m22-m12)/ms**2
		   print "m2-m1: "+str(m22-m12)
		   beta2=getBeta([c0[0](t),c0[1](t),c0[2](t),lam2,c0[4](t),c0[5](t),c0[6](t),m22,lam_S,k,yN],ms,ms)[3]
		   print "b2: "+str([beta2,beta1])

		return (m22,lam2)

	result = match(c0[7](t),c0[3](t),1e-7)
	sol=result
	
	newm= sol[0]
	newl=  sol[1]
	x1=[c0[0](t),c0[1](t),c0[2](t),newl,c0[4](t),c0[5](t),c0[6](t),newm,lam_S,k,yN]
	c10=getCouplings(x1,d1,ms0)
	c1=c10[0]

	V1=getV(c1)
	Vp1=getVp(c10)
	Vpp1=getVpp(c10)
	def Veff(h):
		
		if h < mu:
			return V0(h)
		
		return V1(h)
	def Veffp(h):
		
		if h < mu:
			return Vp0(h)

		return Vp1(h)
	def Veffpp(h):
		
		if h < mu:
			return Vpp0(h)

		return Vpp1(h)
	return [Veff,Veffp,Veffpp]



l1=2.8840315031266117E-012
k1=8.8746503290092427E-015
ms1=10**13.7
V1=getVeff(ms1,l1,k1,0)

d= np.arange(3,18, 0.01)

dom=map(lambda x: 10**x,d)

graph1=map(lambda x: V1[0](x), dom)

# def getRatio(graph):
# 	if graph[0]==0.0:
# 		return -1
# 	fitParams=0
# 	try:
# 		fitParams=getFitParams(d,graph)
# 	except TypeError:
# 		print "BAD FIT"
# 		return -1
# 	# print fitParams
# 	c0=fitParams[0]
# 	c1=fitParams[1]
# 	return c1/c0

plot(d,graph1,"g-")
plot(d,map(lambda x:0,d),"r-")

show()



from potential import *
M=2.43e18
def getEFolds(ms0,lam_S,k,h0):
	mu=ms0
	t=ln(mu)/ln(10)

	# print t
	d0 =np.arange(ln(Mt)/ln(10),19, 0.01)
	x0=[g1,g2,g3,lam,yt,yb,ytau,Mh**2,0,0]
	test=[g1,g2,g3,lam,yt,yb,ytau,Mh**2,0.4,0.1]
	# print test
	c00=getCouplings(x0,d0,1)
	c0=c00[0]
	V0=getV(c0)
	Vp0=getVp(c00)

	d1 = np.arange(t,25.1, 0.01)
	V0mu=Vfunc(c0[7](t),c0[3](t),mu)

	Vpmu=Vp(map(lambda x:float(x(t)),c0[0:-1]),mu,0)

	def matchV(ml):
		Vnew=Vfunc(ml[0],ml[1],mu)
		return -V0mu+Vnew
	def matchVp(ml):
		xsol=[g1,g2,g3,ml[1],yt,yb,ytau,ml[0],lam_S,k]
		Vpnew=Vp(xsol,mu,mu)
		return -Vpmu+Vpnew

	def match(ml):
		return [matchV(ml),matchVp(ml)]
	newm=c0[7](t)
	newl=c0[3](t)
	import scipy.optimize
	try:
		result = scipy.optimize.newton_krylov(match,[newm,newl] , f_tol=1,maxiter=int(1e5))
	except ValueError:
		print "ERROR!"
		def fail(h):return False
		return fail

	sol=result
	
	newm= sol[0]
	newl=  sol[1]
	x1=[c0[0](t),c0[1](t),c0[2](t),newl,c0[4](t),c0[5](t),c0[6](t),newm,lam_S,k]
	c10=getCouplings(x1,d1,ms0)
	c1=c10[0]

	V1=getV(c1)
	Vp1=getVp(c10)

	def V(h):
		if h < mu:
			return V0(h)
		return V1(h)

	def Vpr(h):
		if h < mu:
			return Vp0(h)
		return Vp1(h)
	dom1=map(lambda x:10**x,d1)
	VpList=map(Vpr,dom1)
	# print VpList
	zeros=[]
	def checkZero(x1,x2):
		if x1*x2<=0:
			p1=d1[VpList.index(x1)]
			p2=d1[VpList.index(x2)]
			zero=scipy.optimize.brentq(Vpr,10**p1,10**p2)
			print "NEW ZERO:"+str(zero)
			zeros.append(zero)
		return x2
	reduce(checkZero, VpList,1)

	print zeros
	def VIntegrand(h):
		return Vpr(h)/V(h)

	def eps(h):
		return (M*Vpr(h)/V(h))**2/2

	epsResult=[]
	logh=ln(h0)/ln(10)
	step=-0.0001
	print "eps0:	"+str(eps(10**logh))
	while eps(10**logh)<1:
		newEps=eps(10**logh)
		print newEps
		epsResult.append(newEps)
		logh+=step

	hE=10**logh

	print hE
	from scipy.integrate import quad
	efoldings=quad(VIntegrand,hE,h0)
	
	return efoldings

l1=0.1
k1=0.23337499999999958
ms1=1.1e3

folds=getEFolds(ms1,l1,k1,1.8829201446091267e+17)

print folds 
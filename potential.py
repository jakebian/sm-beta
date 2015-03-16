from functions import *
from couplings import *
from SMParams import *

def getV(couplings):
	lamAt=couplings[3]

	m2At=couplings[7]
	kAt=couplings[9]
	ms=couplings[11]
	lSAt=couplings[8]

	def SVeff(h):
		mu=h
		t=ln(mu)/ln(10)
		mh2=m2At(t)
		lam=lamAt(t)
		k=kAt(t)
		lS=lSAt(t)
		Vs=lam*h**4/4-mh2*h**2/4
		v=246.22
		# print ms
		if h>ms and lS!=0:
			# print lS
			Vs=Vs+1.5*(k*(h**2-v**2)/2)**2/lS
			# a=False
		return Vs

	return SVeff

	

def getVp(coups):
	c=coups[0]
	cp=coups[1]
	lamAt=c[3]
	lampAt=cp[3]
	m2At=c[7]
	m2pAt=cp[7]

	def Vp(h):
		mu=h
		t=ln(mu)/ln(10)

		mh2=m2At(t)
		lam=lamAt(t)
		mh2p=2*m2pAt(t)/mu
		lamp=2*lampAt(t)/mu
		Vs=lam*h**3 -h*mh2/2+h**4*lamp/4-h**2*mh2p/4
		return Vs

	return Vp
def getVpp(coups):
	c=coups[0]
	cp=coups[1]
	lamAt=c[3]
	lampAt=cp[3]
	m2At=c[7]
	m2pAt=cp[7]
	ms=c[11]
	lSAt=c[8]
	kAt=c[9]
	def Vp(h):
		mu=h
		t=ln(mu)/ln(10)

		mh2=m2At(t)
		lam=lamAt(t)
		mh2p=2*m2pAt(t)/mu
		lamp=2*lampAt(t)/mu
		Vs=3*lam*h**2+mh2+2*h**3*lamp+2*h*mh2p
		lS=lSAt(t)
		k= kAt(t)
		
		return Vs

	return Vp
def getCoupDerivs(params,mu,ms):
	b=getBeta(params,mu,ms)
	m=params[7]
	bm=b[7]
	lam=params[3]
	blam=b[3]
	return [2*bm/mu,2*blam/mu]

def Vp(params,mu,ms):
	mh2=params[7]
	lam=params[3]
	h=mu
	der=getCoupDerivs(params,mu,ms)
	mh2p=der[0]
	lamp=der[1]
	VS=lam*h**3-h*mh2/2+h**4*lamp/4-h**2*mh2p/4
	return VS
def Vpp(params,mu,ms):
	mh2=params[7]
	lam=params[3]
	h=mu
	der=getCoupDerivs(params,mu,ms)
	mh2p=der[0]
	lamp=der[1]
	VS=3*lam*h**2+mh2+2*h**3*lamp+2*h*m2hp
	return VS 
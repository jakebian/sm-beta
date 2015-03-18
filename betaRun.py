from couplings import *
from SMParams import *
from potential import *

d0 = (np.arange(2,19, 0.1))
x0=[g1,g2,g3,lam,yt,yb,ytau,Mh**2,0.1,0.3249353,0.512]
c0=getCouplings(x0,d0,1e13)

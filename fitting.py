import numpy as np
from matplotlib.pyplot import *
from scipy.optimize import curve_fit


def getFitParams(d,data):
	minIndex=data.index(min(data))
	minX=d[minIndex]
	mu0=10**minX

	start=minIndex-20	
	end=minIndex+20
	# print(minX)
	print "MIN:"+str(mu0)
	dataX=d[start:end]
	dataY=data[start:end]
	# print("=========Y==========")
	# print(dataY)
	# print("=========ENDY==========")
	# print(dataX[0])
	def func(x, c0, c1):
		mu=10**x
		# print("=========MU==========")
		# print(mu)
		# print("=========ENDMU==========")
		result=c0+c1*((np.log(mu0/mu)**2))
		# print(result)
		return result

	# print dataX
	# print dataY
	popt, pcov = curve_fit(func, dataX, dataY)

	c0=popt[0]
 	c1=popt[1]
	
	# plot(dataX,map(lambda x: func(x,  c0, c1),dataX),'m-')

	return [c0,c1,func]


# print(popt)
# print(pcov)

# c0=popt[0]
# c1=popt[1]
#plot(dataX,map(lambda x: func(x,  c0, c1),dataX),'m-')
# print(popt[1]/popt[0])
# plot(dataX,dataY,"g.")
# plot(dataX,map(lambda x: func(x,  c0, c0*16),dataX),'k--')
# plot(dataX,map(lambda x: func(x,  0, c1),dataX),'m--')

# show()


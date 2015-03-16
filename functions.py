import numpy as np
from numpy.lib.scimath import log
from scipy.special import spence

def ln(x):
	# print(x)
	return np.real(log(x))

def sqrt(x):
	if(x<0):
		return 0
	return np.sqrt(x)

def Li(x):
	return spence(x)

def kill():
	import sys
	sys.exit("stop")
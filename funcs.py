import math

def min (a, b):
	return a if a < b else b

def avg (int_lst):
	return 1.0*sum(int_lst)/len(int_lst)

def med (int_lst):
	int_lst.sort()
	l = len(int_lst)
	if l % 2:
		return int_lst[l / 2]
	else:
		return (int_lst[l/2 - 1] + int_lst[l/2])/2. 

def std (int_lst):
	moy = avg(int_lst)
	dev = [x - moy for x in int_lst]
	dev = [x*x for x in dev]
	var = sum(dev)/len(int_lst)
	return math.sqrt(var)

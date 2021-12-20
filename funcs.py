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
	return -1

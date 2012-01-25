import random
def EUCLID(a,b):
	if b == 0:
		return a
	else:
		return EUCLID(b,a%b)

def POLLARD_RHO(n):
	i = 1
	x = random.randint(0,n-1)
	#print x
	y = x
	k = 2
	while True:
		i = i+1
		x = (x*x-1)%n
		d = EUCLID(y-x,n)
		if d != 1 and d!= n:
			return  d
		if i == k:
			y = x
			k = 2*k

print POLLARD_RHO(82123)



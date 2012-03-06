def levenshtein(s,t):
	K = 2
	d = {}
	S = len(s)
	T = len(t)
	for i in range(S):
		d[i,0] = K*(i)
	for j in range(T):
		d[0,j] = K*(j)
	for j in range(1,T):
		for i in range(1,S):
			d[i,j] = min(d[i-1,j]+K,d[i,j-1]+K,d[i-1,j-1]+abs(ord(s[i-1])-ord(t[j-1])))
	return d

def lev(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(lev(a[1:], b[1:])+(a[0] != b[0]), lev(a[1:], b)+1, lev(a, b[1:])+1)

s = 'cmc'
t = 'snmn'
print levenshtein(s,t)

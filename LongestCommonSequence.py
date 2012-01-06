class LCS:
	def __init__(self,X,Y):
		self.X = X
		self.Y = Y
		self.c = [[0 for col in range(len(self.Y)+1)] for row in range(len(self.X)+1)]

	def lcs_length(self):
		for x in range(1,len(self.X)):
			for y in range(1,len(self.Y)):
				if self.X[x-1] == self.Y[y-1]:
					self.c[x][y] = self.c[x-1][y-1] +1
				else:
					self.c[x][y] = max(self.c[x][y-1],self.c[x-1][y])
	
	def lcs(self,m,n):
		if m == 0 or n == 0:
			return
		elif self.X[m-1] == self.Y[n-1]:
			print self.X[m-1]
			return self.lcs(m-1,n-1) 			
		else:
			if self.c[m][n-1] > self.c[m-1][n]:
				return self.lcs(m,n-1)
			else:
				return self.lcs(m-1,n)


X = ['A','A','T','C','G','A']
Y = ['A','C','A','C','B','G']
lcs = LCS(X,Y)
lcs.lcs_length()
print lcs.c
lcs.lcs(len(X),len(Y))
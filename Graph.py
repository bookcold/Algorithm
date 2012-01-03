class Graph:
	def __init__(self,G):
		self.G = G
	
	def V(self):
		return self.G.keys()

	def Adj(self,V):
		return self.G[V].keys()

	def Weight(self,u,v):
		return self.G[u][v]
	
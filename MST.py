from sys import *
from UnionFind import UnionFind

class Graph:
	def __init__(self,G):
		self.G = G
		self.keys = {}
		self.parents = {}
	
	def V(self):
		return self.G.keys()

	def Adj(self,V):
		return self.G[V].keys()

	def Weight(self,u,v):
		return self.G[u][v]

	def prim(self,r):
		for v in self.V():
			self.keys[v] = maxint
			self.parents[v] = None
		self.keys[r] = 0
		queue = self.keys
		while queue:
			u = queue.keys()[0]
			for node in queue.keys():
				if queue[u] > queue[node]:
					u = node
			#print queue[u]
			del queue[u]
			for v in self.Adj(u):
				if v in queue and self.Weight(u,v) < self.keys[v]:
					self.parents[v] = u
					self.keys[v] = self.Weight(u,v)
		return self.parents

	def kruskal(self):
		Weight = {}
		Trees = []
		UnionSet = UnionFind()
		UnionSet.makeset(self.V())
		for v in self.V():
			edge = self.Adj(v)
			for u in edge:
				uv = u + v
				Weight[uv] = self.Weight(u,v)

		#edges = [(self.Weight(u,v),u,v) for v in self.V() for u in self.Adj(v)].sort()
		edges = [(self.Weight(u,v),v,u) for v in self.V() for u in self.Adj(v)]
		edges.sort()
		for w,u,v in edges:
			if UnionSet.find(u) != UnionSet.find(v):
				Trees.append(u+v)
				UnionSet.union(u,v)
		return Trees	

L = {'A': {'B':4, 'H':8}, 'B': {'A':4, 'C':8, 'H':11},
		'C': {'B':8, 'D':7, 'I':2, 'F':4}, 'D': {'C':7,'F':14, 'E':9},
		'E': {'D':9, 'F':10}, 'F': {'C':4, 'D':14, 'E':10, 'G':2}, 
		'G':{'H':1,'F':'2','I':6}, 'H':{'A':8,'B':11,'I':7,'G':1},
		'I':{'C':2,'H':7,'G':6}
	}
G = Graph(L)
print G.kruskal()
print G.prim('A')



class UnionFind:
	def __init__(self):
		self.root = []

	def __print__(self):
		print self.root
	
	def makeset(self,object):
		for t in object:
			self.root.append([t])

	def union(self,u,v):
		left = []
		right = []
		for unionset in self.root:
			if u in unionset:
				left = unionset
			if v in unionset:
				right = unionset
		self.root.append(left+right)
		self.root.remove(left)
		self.root.remove(right)

	def find(self,u):
		for unionset in self.root:
			if u in unionset:
				return unionset
		return []
from Tree import Tree

class Huffman:
	def __init__(self,listnodes):
		self.root = None

		self.forest = [Tree(None,None,key,value) for key,value in listnodes.items()]
	
	def construct_huffman(self):
		length = len(self.forest)
		for t in range(0,length-1):
			left,right = self.get_min_value_node()
			#newtree = Tree(self.forest[left],self.forest[right],self.forest[left].name+self.forest[right].name,
			#	self.forest[left].value+self.forest[right].value)
			newtree = Tree(left,right,left.name+right.name,left.value+right.value)
			self.forest.remove(left)
			self.forest.remove(right)
			self.forest.append(newtree)
		print self.forest
		return self.forest[0]

	def get_min_value_node(self):
		minnode = (self.forest[0].value > self.forest[1].value) and self.forest[1] or self.forest[0]
		secnode = (self.forest[0].value > self.forest[1].value) and self.forest[0] or self.forest[1]
		for t in self.forest:
			if t.value < minnode.value:
				if secnode.value > minnode.value:
					secnode = minnode
				minnode = t
			elif t.value < secnode.value & t.value != minnode.value:
				secnode = t
		return minnode,secnode

	def get_node_index(self,node):
		for t in range(len(self.forest)):
			if self.forest[t].name == node.name:
				return t


listnodes = {'f':5,'e':9,'c':12,'b':13,'d':16,'a':45}
H = Huffman(listnodes)
root = H.construct_huffman()
print root.value,root.name


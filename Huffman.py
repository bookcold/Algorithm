from Tree import Tree

class Huffman:
	def __init__(self,listnodes):
		self.forest = [Tree(None,None,key,value) for key,value in listnodes.items()]
	
	def construct_huffman(self):
		length = len(self.forest)
		for t in range(0,length-1):
			left,right = self.get_min_value_node()
			#print "left:" + str(left.name)
			#print "right:" + str(right.name)
			newtree = Tree(left,right,left.name+right.name,left.value+right.value)
			self.forest.remove(left)
			self.forest.remove(right)
			self.forest.append(newtree)		
		return self.forest[0]

	def get_min_value_node(self):
		minnode = self.forest[0]
		s_minnode = self.forest[1]
		for t in self.forest:
			if t.value < minnode.value:
				s_minnode = minnode
				minnode = t
			elif t.value > minnode.value and t.value < s_minnode.value:
				s_minnode = t
		return minnode,s_minnode


listnodes = {'f':5,'e':9,'c':12,'b':13,'d':16,'a':45}
H = Huffman(listnodes)
root = H.construct_huffman()
#Tree.bfs(root)
Tree.dfs(root)
#print root.value,root.name


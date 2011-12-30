class Tree:
	def __init__(self,left,right,name,value):
		self.left = left
		self.right = right
		self.name = name
		self.value = value
	
	@classmethod
	def bfs(self,root):
		queue = []
		queue.append(root)
		while len(queue) != 0:
			node = queue.pop(0)
			print node.name + ":" + str(node.value)
			if node.left != None:
				queue.append(node.left)
			if node.right != None:
				queue.append(node.right)

	@classmethod
	def dfs(self,root):
		if root != None:
			print root.name + ":" +str(root.value)
			self.dfs(root.left)
			self.dfs(root.right)

		
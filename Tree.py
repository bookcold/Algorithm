class Tree:
	def __init__(self,left,right,name,value):
		self.left = left
		self.right = right
		self.name = name
		self.value = value
	
	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def get_name(self):
		return self.name

	def get_value(self):
		return self.value
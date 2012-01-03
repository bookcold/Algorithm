from Graph import Graph

class Dijkstra:
	def __init__(self,G):
		self.G = Graph(G)

	def Dijkstra(self,start):		
		dist = {}   
		previous = {}
		Q = {}
		# Initializations
		# dist: Unkown distance function from souce to v
		# previous: Previous node in optimal path from source
		for v in self.G.V():
			dist[v] = float('inf')
			previous[v] = float('inf')
			Q[v] = float('inf')
		dist[start] = 0
		Q[start] = 0

		while Q: # the main loop
			u = min(Q, key = lambda x:Q.get(x))
			if dist[u] == float('inf'): 
				break  # all remaining vertices are inaccessible from souce
			Q.pop(u)
			# where v has not yet been removed from Q
			for adj in self.G.Adj(u):
				alt = dist[u] + self.G.Weight(u,adj)
				#replace with optimal distance and node
				if alt < dist[adj]:
					dist[adj] = alt
					Q[adj] = alt
					previous[adj] = u
		return dist,previous
	
	def shortest_path(self,start,end):
		path = []
		dist,previous = self.Dijkstra(start)
		print dist,previous
		#get the path from start to end
		while 1:
			if end == float('inf'):
				break
			path.insert(0,end)
			end = previous[end]
		return path



G = {'A': {'B':4, 'H':8}, 'B': {'A':4, 'C':8, 'H':11},
		'C': {'B':8, 'D':7, 'I':2, 'F':4}, 'D': {'C':7,'F':14, 'E':9},
		'E': {'D':9, 'F':10}, 'F': {'C':4, 'D':14, 'E':10, 'G':2}, 
		'G':{'H':1,'F':2,'I':6}, 'H':{'A':8,'B':11,'I':7,'G':1},
		'I':{'C':2,'H':7,'G':6}
	}
dijk = Dijkstra(G)
print dijk.shortest_path('E','A')
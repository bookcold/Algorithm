from PriorityDictionary import PriorityDictionary
def Dijkstra(G,start,end=None):
	D = {}	# dictionary of final distances
	P = {}	# dictionary of predecessors
	Q = PriorityDictionary()
	Q[start] = 0

	for v in Q:
		D[v] = Q[v]
		if v == end: break

		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError
				elif w not in Q or vwLength < Q[w]:
					Q[w] = vwLength
					P[w] = v
	return (D,P)

def shortestPath(G,start,end):
	D,P = Dijkstra(G,start,end)
	Path = []
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	return Path



G = {'A': {'B':4, 'H':8}, 'B': {'A':4, 'C':8, 'H':11},
		'C': {'B':8, 'D':7, 'I':2, 'F':4}, 'D': {'C':7,'F':14, 'E':9},
		'E': {'D':9, 'F':10}, 'F': {'C':4, 'D':14, 'E':10, 'G':2}, 
		'G':{'H':1,'F':'2','I':6}, 'H':{'A':8,'B':11,'I':7,'G':1},
		'I':{'C':2,'H':7,'G':6}
	}

shortestPath(G,'A','H')
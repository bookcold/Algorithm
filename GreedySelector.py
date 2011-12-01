def GreedySelector(action):
	selector = {}
	selector[action.keys()[0]] = True
	j = 0
	count = 1
	for k in range(1,len(action)):
		print k,j
		if action[action.keys()[k]][0] >= action[action.keys()[j]][1]:
			selector[action.keys()[k]] = True
			j = k
			count += 1
		else:
			print k
			selector[action.keys()[k]] = False
	return selector,count

actions = {'A':[1,4],'B':[3,5],'C':[0,6],'D':[5,7],'E':[3,8],
		'F':[5,9],'G':[6,10],'H':[8,13],'I':[8,12],'J':[2,13],'K':[12,14]}
print GreedySelector(actions)




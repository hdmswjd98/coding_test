def dfs(n):
	global G, T, V
	V[n] = True
	for e in G[n]:
		if (V[e] == False):
			T[n].append(e)
			dfs(e)
def Go(n):
	global C, T
	mm= 1
	for e in T[n]:
		mm += Go(e)
	C[n] = mm
	return mm

def solution(n, w):
	global G, T, V, C
	G, T, C, V =[], [], [0]*n, [False]*n
	for i in range(n):
		G.append([])
		T.append([])
	for e in w :
		n1, n2 = e[0]-1, e[1]-1
		G[n1].append(n2)
		G[n2].append(n1)
	dfs(0)
	Go(0)
	mm = n
	for e in C:
		mm = min(mm, abs(n-e -e))
	return mm
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
#def Eval 부분만 해보기 

def Eval():
	global mm, D, K, A, N
	cur, left =0, K
	for e in A:
		if (left < D[e][0]):
			break
		cur +=1
		left -= D[e][1]
#	print(A, cur)
	mm = max(cur, mm) 

def perm(n):
	global N, V, A
	if (n==N):
		Eval()
		return
	for i in range(N):
		if (V[i] == True):
			continue
		A[n], V[i] = i, True
		perm(n+1)
		V[i]=False

def solution(k, dg):
	global N, V, D, K, A, mm
	D, N, K, mm = dg, len(dg), k, 0
	V, A = [False]*N, [-1]*N
	perm(0)
	return mm

print(solution(80, [[80,20],[50,40],[30,10]]))
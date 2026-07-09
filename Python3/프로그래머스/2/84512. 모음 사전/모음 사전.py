def Eval():
	global A, vowels
	tt =''
	for e in A:
		tt = tt + e
		W.add(tt)

def dfs(n):
	global A
	if (n == 5):
		Eval()
		return
	for e in vowels:
		A[n] = e
		dfs(n+1)

def solution(word):
	global A, W, vowels
	vowels ="AEIOU"
	W, A = set([]), [-1]*5
	dfs(0)
	W = list(W)
	W.sort()
	return (W.index(word)+1)

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
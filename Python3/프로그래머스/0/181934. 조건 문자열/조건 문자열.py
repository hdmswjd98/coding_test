def solution(ineq, eq, n, m):
    answer = 0

    if (ineq==">" and eq=="="):
        if(n>=m):
            return 1
        else:
            return 0
        
    if (ineq=="<" and eq=="="):
        if(n<=m):
            return 1
        else:
            return 0

    if (ineq==">" and eq=="!"):
        if(n>m):
            return 1
        else:
            return 0

    if (ineq=="<" and eq=="!"):
        if(n<m):
            return 1
        else:
            return 0
            
    return answer

print(solution("<",	"=",	20,	50))
print(solution(">"	,"!"	,41	,78))
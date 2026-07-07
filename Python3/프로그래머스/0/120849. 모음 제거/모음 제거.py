# vowel = set(list("aeiou"))
# 검색시간이 줄어듦 (데이터가 많아졌을 시)



def solution(my_string):
    vowel = set(list("aeiou"))
    ans=[]

    for cc in my_string:
        if((cc in vowel)==False):
            ans.append(cc)

    return (''.join(ans))
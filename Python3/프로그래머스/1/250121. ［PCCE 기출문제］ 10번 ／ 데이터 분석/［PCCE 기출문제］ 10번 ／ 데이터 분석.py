def solution(data, ext, val_ext, sort_by):
    dic = {"code":0, "date":1, "maximum":2, "remain":3}
    nn = dic[ext]
    answer = []

    for e in data:
        if(e[nn] < val_ext):
            answer.append(e)
    nn = dic[sort_by]
    answer.sort(key=lambda x:x[nn])
    return answer
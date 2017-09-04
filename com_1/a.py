def solution(land):
    answer = 0
    d = land[0].index(min(land[0]))
    
    for a in land:
        print(a)
        a[d] = -1
        m = max(a)
        answer = answer + m
        d = a.index(m)
        print(a)

    return answer

print(solution([[2,2,3,2],[5,6,7,8],[4,3,2,1]]))



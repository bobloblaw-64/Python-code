def nextRound(k,scores):
    scores.sort(reverse=True)
    k_score = scores[k - 1]
    n = 0
    for i in scores:
        if i >= k_score and i != 0:
            n += 1
    return n
print(nextRound(5,[10,9,8,7,6,6,6,5,4]))
print(nextRound(2,[0,0,0,0]))
print(nextRound(2,[1,1,1,1]))
print(nextRound(20,[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))
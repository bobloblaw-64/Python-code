def bitshift(s,k,b):
    k = k % len(s)
    
    if b: #if b is true this is a left shift
        answer = s[k:] + s[:k]
        
    else:
        answer = s[-k:] + s[:-k]
        
    return answer 

print(bitshift("110011",2,True))
        
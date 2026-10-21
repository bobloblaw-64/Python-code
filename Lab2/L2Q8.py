def odd_finder(a,b,c,d,e,f,g,h,i,j):
    input_list = [a,b,c,d,e,f,g,h,i,j]
    n = 0
    for i in range(len(input_list)):
        if input_list[i] > 0 and input_list[i] % 2 != 0:
            n += 1
            
    return n

print(odd_finder(1,2,3,4,5,-1,-2,-3,-4,0))
def singleDigit(N):
    n_str = str(N)
    
    while True:
        current_sum = 0
        for digit in n_str:
            current_sum += int(digit)
        if len(str(current_sum)) == 1:
            return current_sum
        n_str = str(current_sum)
        
    
        

print(singleDigit(198))


        
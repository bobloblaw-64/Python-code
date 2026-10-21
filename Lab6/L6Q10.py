def composite2(N):#finds the Nth composite odd number
    def is_prime(num):
        if num >=2:
            
            if num == 2:
                return True
            for i in range(2, num - 1):
                if num % i == 0:
                    return False
            return True
        else:
            return None
        
    
    comp_odds = []
    x = 0
    
    while True:
        x += 1
        current_odd = 2 * x + 1
        if is_prime(current_odd):
            continue
        else:
            comp_odds.append(current_odd)
            if len(comp_odds) == N:
                return comp_odds[-1]
            
print(composite2(167))
            
            
            
        
        
        
        
        
        
        
        
        
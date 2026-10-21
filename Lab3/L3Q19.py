def gcd(num1,num2):
    if num1 >= num2:
        r = num1
    else:
        r = num2
    for i in range(1, r+1):
        if num1 % i == 0 and num2 % i == 0:
            current_gcd = i
            
    return current_gcd

 	

print(gcd(18,12))
        
n = int(input())
#Don't change the above line of code. Write your program below this line. Remember to print the final result only.
list = [0 , 1 , 1]

if n <= 0:
    print(0)

elif n <= 3:
    print(list[n-1])

else:
    while len(list) < n:
        list.append(list[-1] + list[-2])
    print(list[-1])

    
    
    
    
    
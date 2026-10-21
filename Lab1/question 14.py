n = int(input())
#Don't change the above line of code. Write your program below this line. Remember to print the final result only.
fib_list = [0 , 1 , 1]
sum_list = [0]

#if n <= 0:
    #print(0)

if n >= 3:
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
if n > 0:
    for i in range(n):
        sum_list.append(sum_list[-1] + fib_list[i])
    del sum_list[1]

print(sum_list[-1]) 
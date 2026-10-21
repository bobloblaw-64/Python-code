n = int(input())
# write your program below
y = 0
if n >= 1:
    for i in range(n):
        y = y + (2 * i + 1)
        
    print(y)
else:
    print(0)
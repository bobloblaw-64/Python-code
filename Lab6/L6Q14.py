def sequence(n):
    current_n = n
    seq_lst = [n]
    while True:
        if current_n % 2 == 0:
            current_n = current_n / 2
        else:
            current_n = 3 * current_n + 1
        seq_lst.append(int(current_n))
        if current_n == 1:
            return seq_lst
        
print(sequence(1))  
            
def list_swap(lst):
    output = lst.copy()
    even_len = len(lst)
    if even_len % 2 != 0:
        even_len -= 1
    i = 0
    while i < even_len:
        output[i] = lst[i + 1]
        output[i + 1] = lst[i]
        i += 2
    return output
print(list_swap([1,2,3,4]))
print(list_swap([12,32,54,24,51,23.54]))

        
        
    
        
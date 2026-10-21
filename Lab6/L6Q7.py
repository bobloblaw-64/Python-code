def long_enough(strings, min_length):
    out_lst = []
    for string in strings:
        if len(string) >= min_length:
            out_lst.append(string)
            
    return out_lst
            
strings = ['a', 'bc', 'def', 'ghij', 'klmno']
print(long_enough(strings, 3))
def compare_strings(string1, string2):
    if string1[0] == string2[0]:
        if len(string1) == len(string2):
            return 'error'
        elif len(string1) >= len(string2):
            return string1
        else:
            return string2
        
    else:
        if string1[-1] == string2[-1]:
            return 'error'
        elif string1[-1] > string2[-1]:
            return string1
        else:
            return string2
        
print(compare_strings("sky", "cloud"))
        
    
                
    
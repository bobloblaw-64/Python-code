with open('stock.csv') as file:
    answer = []
    ans_str = ''
    for line in file:
        row = line.strip().split(',')
        answer.append(row[0])
        
    for value in answer:
        x = ans_str + value + ','
        ans_str = x
    
    print(ans_str[:-1])
        
        

    
    

            
    

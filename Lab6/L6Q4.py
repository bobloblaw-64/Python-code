def make_index(words_on_page): 
    output_dic = {}
    for page, words_lst in words_on_page.items():
        
        for word in words_lst:
            
            if word in output_dic:
                output_dic[word].append(page)
            else:
                output_dic[word] = [page]
    
    return output_dic

input_dict = {
   1: ['hi', 'there', 'fred'], 
   2: ['there', 'we', 'go'],
   3: ['fred', 'was', 'there']}
output_dict = make_index(input_dict)
for word in sorted(output_dict.keys()):
    print(word + ': ' + str(output_dict[word]))
            

        
    
    

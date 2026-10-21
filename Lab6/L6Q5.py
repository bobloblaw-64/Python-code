
def make_dictionary(filename): 
    out_dict = {}
    with open(filename, 'r') as in_file:
        
        for line in in_file:
            item = line.strip()
            if item == '':
                continue
            elif item in out_dict:
                out_dict[item] += 1
            else:
                out_dict[item] = 1
                
    return out_dict

# Testing with the example data in the question
dictionary = make_dictionary('jolly.txt')
for key in sorted(dictionary.keys()):
    print(key + ': ' + str(dictionary[key]))

        
        
    
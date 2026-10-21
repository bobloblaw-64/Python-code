def find_key(input_dict, value):
    output = None
    for key in input_dict.keys():
        if input_dict[key] == value:
            output = key
            break
    return output

test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'b'))

test_dictionary = {100:'a', 20:'b', 3:'c', 400:'d'}
print(find_key(test_dictionary, 'e'))
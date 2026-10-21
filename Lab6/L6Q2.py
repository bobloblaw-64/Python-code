def word_counter(input_str):
    lower_str = input_str.lower()
    sen_lst = lower_str.split()
    word_dict = {}

    for word in sen_lst:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
    return word_dict


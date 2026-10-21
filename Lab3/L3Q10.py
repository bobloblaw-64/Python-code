def double_list(items):
    if len(items) % 2 == 0:
        return items + items
    else:
        items.append(items[-1])
        return items
    
print(double_list([1, 2, 3, 4, 5, 6, 7, 8]))
print(double_list([1, 1, 2, 2, 3, 4, 5, 5, 6]))
def my_enumerate(items):
    i = 0
    out_lst = []
    for item in items:
        out_lst.append((i, item))
        i += 1
    return out_lst

ans = my_enumerate(['a', 1, 'den'])
print(ans)
        
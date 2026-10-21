def series(x):
    ser_sum = 0
    n = 0
    while True:
        term = (1 / (2 ** n))
        if term < x:
            return round(ser_sum, 4)
        ser_sum += term
        n += 1
        
print(series(0.01))
        
        

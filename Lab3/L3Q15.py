def check_temperature(temperature, limit):
    temp_in_f = temperature * (9 / 5) + 32
    if limit > temp_in_f:
        return True
    else:
        return False
    
print(check_temperature(30.0, 140.0))
print(check_temperature(30.0, 80.0))
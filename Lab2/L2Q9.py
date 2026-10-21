def virus_growth(num,rate,hour,time):
    return num * (rate ** (time / hour))

print(round(virus_growth(100,2,4,16),1))



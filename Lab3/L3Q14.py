def hunting_animals(weather, animal, n):
    if weather == 'sunny':
        if animal == 'rabbit':
            return n
        else:
            return int(n / 2)
        
    else:
        if animal == 'rabbit':
            return int(n / 2)
        else:
            return int(n / 3)

print(hunting_animals("sunny", "rabbit", 6))
print(hunting_animals("sunny", "deer", 6))
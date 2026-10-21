def dseries(n_terms):
    sigma = 0
    for i in range(n_terms + 1):
        sigma += (i ** 2)
    return sigma

print(dseries(4))
        
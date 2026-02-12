def fun(a):
    return a % 2 == 0

sequence = [1, 2, 3, 4, 5, 10.0, 7.5]
filtered = list(filter(fun, sequence))

print(filtered)

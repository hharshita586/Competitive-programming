def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
num = 5

print(fact(num))
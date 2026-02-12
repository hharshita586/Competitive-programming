def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)
num = 2
p = 5
print(power(num, p))
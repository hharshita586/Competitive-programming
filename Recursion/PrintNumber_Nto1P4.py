def print_nums(n):
    if n == 0:
        return
    print(n)
    print_nums(n - 1)
num = 5
print_nums(num)
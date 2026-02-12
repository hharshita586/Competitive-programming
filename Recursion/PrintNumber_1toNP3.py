def print_nums(n):
    if n == 0:
        return
    print_nums(n - 1)

    print(n)
num = 5
print_nums(num)
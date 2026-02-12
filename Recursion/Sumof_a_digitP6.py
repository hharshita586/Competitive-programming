def sum_digits(num):
    if num < 10:
        return num
    return (num % 10) + sum_digits(num // 10)
n = 1234
print(sum_digits(n))
def count_digits(n):
    
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
num = 12345
print(count_digits(num))
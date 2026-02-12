def reverse_str(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse_str(s[:-1])
text = "hello"
print(reverse_str(text))
A = input("Enter string: ")
A = A * 2
result = ""
for ch in A:
    if ch.islower():
        if ch in "aeiou":
            result += "#"
        else:
            result += ch

print(result)

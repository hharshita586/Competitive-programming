a = input()
count = 0
for i in range(len(a) - 2):
    if a[i] == "b" and a[i+1] == "o" and a[i+2] == "b":
        count += 1
print(count)

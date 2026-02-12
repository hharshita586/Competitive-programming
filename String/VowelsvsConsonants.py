t = int(input())

for i in range(t):
    s = input()
    v = 0
    for ch in s:
        if ch in 'aeiouAEIOU':
            v += 1
    print(v, len(s) - v)

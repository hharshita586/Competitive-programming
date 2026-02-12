n = int(input())
codes = list(map(int, input().split()))

unique = []
for x in codes:
    if codes.count(x) == 1:
        unique.append(x)

if unique:
    print(*unique)
else:
    print(-1)

n = int(input())
ids = list(map(int, input().split()))

res = [x for x in ids if x % 5 == 0]

if res:
    print(*res[::-1])
else:
    print(-1)

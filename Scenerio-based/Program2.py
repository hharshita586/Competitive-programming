n = int(input())
ids = list(map(int, input().split()))

even_ids = [x for x in ids if x % 2 == 0]

if even_ids:
    print(*even_ids)
else:
    print(-1)

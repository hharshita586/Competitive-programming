n = int(input())
att = list(map(int, input().split()))

max_streak = 0
current = 0

for x in att:
    if x == 0:
        current += 1
        max_streak = max(max_streak, current)
    else:
        current = 0

print(max_streak)

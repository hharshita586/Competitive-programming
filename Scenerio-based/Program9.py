n = int(input())
temps = list(map(int, input().split()))

avg = sum(temps) / n

count = 0
for t in temps:
    if t > avg:
        count += 1

print(count)

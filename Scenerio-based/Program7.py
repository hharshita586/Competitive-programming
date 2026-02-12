n = int(input())
prices = list(map(int, input().split()))

count = 0
for i in range(1, n):
    if prices[i] > prices[i - 1]:
        count += 1

print(count)

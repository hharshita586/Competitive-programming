n = int(input())
count = 0
for i in range(n):
    data = list(map(int, input().split()))
    marks = data[0]
    attendance = data[1]
    if marks >= 75 and attendance >= 80:
        count += 1
print(count)


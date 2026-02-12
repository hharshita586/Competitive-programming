n = int(input())
marks = list(map(int, input().split()))

passed = 0
for m in marks:
    if m >= 35:
        passed += 1

failed = n - passed
print(passed, failed)

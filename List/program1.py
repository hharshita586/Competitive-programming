N=int(input())
Marks=list(map(int, input().split()))
passed = 0
failed = 0

for mark in Marks:
    if mark >= 35:
        passed = +1
    else:
        failed = +1
        
print(passed, failed)
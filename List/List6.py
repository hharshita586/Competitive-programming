#For arrayA,youhavetofindthevalueofabsolutedifferencebetweenthecountsof
#evenandoddelementsinthearray.
#Input:
#A=[1234]
#Output:
#0

a = list(map(int, input().split()))
even=0
odd=0
for i in a:
    if(i%2==0):
        even +=1
    else:
        odd+=1
diff=even-odd
print(diff)
# YouaregivenanintegerarrayA.
#Youhavetoprint theoddandevenelementsofarrayAin2separatelines.
#Input:
#A=[12345]
#Output:
#1 3 5
#2 4

a = list(map(int, input().split()))
even=0
odd=0
for i in a:
    if(i%2==0):
        print(i,end=" ")
print()
for i in a:
    if(i%2!=0):
        print(i,end=" ")
print()

a=list(map(int,input().split()))
arr.sort()
a1=arr[-1]
a2=arr[-2]
sum=0
avg=(a1+a2)/2
for i in range(len(arr)):
    if arr[i]<avg:
        arr[i]=0
for i in range(len(arr)):
    sum=arr[i]
print(sum)

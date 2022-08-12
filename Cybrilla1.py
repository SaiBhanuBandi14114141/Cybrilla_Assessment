n,k=input().split()
n,k=int(n),int(k)
arr=input().split()
result=0
for i in range(k):
    if arr.count(max(arr))==1:
        result+=int(max(arr))
        arr.remove(max(arr))
    else:
        c=arr.count(max(arr))
        for i in range(c):
            result+=int(max(arr))

print(result)

    

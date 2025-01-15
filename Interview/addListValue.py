def equalToTarget(arr,target):
    l1=[]
    for i in range(len(arr)):
        a=(target-arr[i])
        l1.append(a)
    common = list(set(l1) & set(arr))
    return common
arr=[3,2,4,7,8]
target=9
a=equalToTarget(arr,target)
print(a)
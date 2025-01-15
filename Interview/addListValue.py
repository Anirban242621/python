def equalToTarget(arr,target):
    l1=[]
    for i in range(len(arr)):
        a=(target-arr[i])
        l1.append(a)
    common = list(set(l1) & set(arr))
    if len(common)==0:
        return False
    return common
arr=[30,2,4,7,8]
target=9
a=equalToTarget(arr,target)
if a!=False:
    print("Found such pair which can match the Target: ",a)
else:
    print("No such pair found")
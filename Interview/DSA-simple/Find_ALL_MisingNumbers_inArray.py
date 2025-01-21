arr=[4,3,2,7,8,2,3,1]
num=set(arr)
l=[]
for i in range(1,len(arr)+1):
    if i not in num:
        l.append(i)
print("The provided array is: ",arr)
print("After removing duplicate values in array: ",list(num))
print("Missing Numbers:",l)
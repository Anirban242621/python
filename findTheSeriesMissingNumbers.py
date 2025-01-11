def find_missing_numbers(arr, end): 
    missing_numbers = []
    for i in range(1, end+1):
        if i not in arr:
            missing_numbers.append(i)
    return missing_numbers 
def sort(arr):
    n=len(arr)
    for i in range(n):
        # print("current value of I: ",i)
        # print("Current logic value: ",n-i-1)
        for j in range(0, n-i-1): # Swap if the element found is greater than the next element 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [1, 2, 4, 9, 7,6, 10] 
print("The List provided :",arr)
sort(arr)
end = arr[len(arr)-1]
print("After sort:",arr)
missing_numbers = find_missing_numbers(arr, end) 
print("Missing number:",missing_numbers) 
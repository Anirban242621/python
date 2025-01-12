def fibonacci(n):
    l=[]
    for i in range(0,n):
        if i==0 or i==1:
            l.append(i)
        else:
            l.append(l[i-1]+l[i-2])
    return l
    
n=int(input("Enter the number of terms: "))
# print(type(n))
fib=fibonacci(n)
print("Fibonacci sequence:", fib)
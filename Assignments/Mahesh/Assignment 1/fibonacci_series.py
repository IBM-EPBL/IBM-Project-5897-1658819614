a = 0
b = 1
n = int(input("Enter no of elements in fibonacci : "))
print("List of the fibonacci series are : ")
print(a, end = " ")
print(b, end = " ")
for i in range(0,n-2):
    fib = a + b
    print(fib, end = " ")
    a = b
    b = fib

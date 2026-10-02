# Bubble sort

a = eval(input("Enter a list: "))
n = len(a)

for i in range(n):
    for j in range(n-i-1):
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print("After sorting: ",a)

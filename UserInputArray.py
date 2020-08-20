from array import *

arr = array('i', [])

arrLen = int(input("Enter the length of Array: "))

for i in range(arrLen):
    x = int(input("Enter the Next Value: "))
    arr.append(x)
print(arr)
y = int(input("Enter the number to search the index: "))
print(arr.index(y))
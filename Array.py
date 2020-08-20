from array import *
vals = array('i', [5, -9, 8, 2])
newArr = array(vals.typecode, (a**2 for a in vals))

print (vals)
print (newArr)

List1 = [2,4,5,7,9]
List2 = ([a**2 for a in List1])

print(List1)
print(List2)
print(type(List2))
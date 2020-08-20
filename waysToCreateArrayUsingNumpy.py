#############################
## Ways to create an Array
# array()
# linspace()
# logspace()
# arange()
# zeros()
# ones()
##############################
from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([1,2,3,4,5.0])
print(arr1.dtype)
print(arr2.dtype)

arr3 = linspace(0,15,16) # Start,End:Included,Parts: Default is 50
print("linspace Array:",arr3)

arr4 = arange(1,15,2) # Start,End,Increment
print("arange Array:",arr4)

arr5 = logspace(1,40,5)
print("logspace Array:",arr5)
print("logspace Array upto 2 decimal:",'%.2f' %arr5[0])

arr6 = zeros(10,int) #default type is float
print("zeros Array:",arr6)

arr7 = ones(10,int) #default type is float
print("ones Array:",arr7)
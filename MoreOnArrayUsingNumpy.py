from numpy import *
arr1 = array([1,2,3,9,7,6])
arr2 = array([3,5,6,8,9,1])
# arr1 = arr1 + 5 # add value to each element of array
# print("Adding 5 to each element of Array:", arr1)
# arr3 = arr1 + arr2
# print("Addition of 2 Arrays:", arr3)
# print("Sin of Array:", sin(arr3))
# print("Cos of Array:", cos(arr3))
# print("Square root of Array:",(sqrt(arr3)))
# sum(arr1), min(arr1), max(arr1), average(arr1), sort(arr1), unique(arr1)
# print(mean(arr1))
# print(median(arr1))
# print(concatenate([arr1,arr2]))
# arr3 = arr1 # address of both Arrays are same
# print(id(arr1),id(arr3))
# arr4 = arr1.view() #any change in Arr1 will reflect in Arr4
arr5 = arr1.copy() # change in Arr1 will not reflect in Arr5
arr1[1] = 7
#print(id(arr5))
print(arr1,arr5)
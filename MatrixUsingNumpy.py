from numpy import *
arr1 = array([
                [1, 2, 3],
                [4, 5, 6]

            ])

#print(arr1.size)
#print(arr1.shape)
#print(arr1.dtype)
#print(arr1.ndim)
# Converts Multi Dim Array into 1D Array
#arr2 = arr1.flatten()
# 2R6C converts into 3R4C
#arr3 = arr1.reshape(3,4)
# 2R6C converts into 3D Array
#arr4 = arr1.reshape(2,2,3)
m1 = matrix(arr1)
m2 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
#print(diagonal(m2))  #To get Diagonal elements
m3 = m1*m2
print(m3)


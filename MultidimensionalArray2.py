from numpy import *
array = array([
    [1,2,3,4],
    [1,2,4,7],
    [5,3,5,9]
])
print(array)
arr = array.flatten()
print(arr)
arr2 = arr.reshape(2,6)
print(arr2)
arr3 = arr2.reshape(3,4)
print(arr3)

arr4 = arr3.reshape(2,2,3)
print(arr4)

from numpy import *
arr = matrix('1,2,3;4,5,6;8,9,0')
print(arr)
arr2 = matrix('1,2,3;4,5,6;8,9,0')
result = arr * arr2
print(result)
arr3 = matrix('1,2,3,4,5;5,6,7,8,9')
print(arr3)
print(diagonal(arr3))
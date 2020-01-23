from array import *

array = array('i', [])

number = int(input("Enter the range of the array: "))

for i in range (number):
    x = int(input("Enter the next values: "))
    array.append(x)

print(array)

val = int(input("Insert the desired value: "))

k = 0
for a in range (number):
    if a==val:
        print(k-1)
        break

    k+=1


print(array.index(val))


nums = [1,23,454,65,34,2,65,3]

for i in nums:
    if i % 22 == 0:
        print(i)
        break

else:
    print("Nothing is found")
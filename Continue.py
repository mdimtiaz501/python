number = int(input("Enter a number within 1 to 20: "))

for i in range(1, number):
    if i> 20:
        break
    if i% 3 ==0:
        continue
    print(i)

print("the END")




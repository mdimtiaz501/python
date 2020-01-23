num = int(input("Enter a number within 1 to 10: "))

for i in range(1,num):
    if i> 10:
        break
    print(i)
    i+=i

print("The END")
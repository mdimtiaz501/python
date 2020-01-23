def check(parameter):
    even = 0
    odd = 0
    for i in parameter:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

list = [1,2,4,5,23,5,346,345,2345,57,6,45,343,6,57,3,4]
even, odd = check(list)

print("Even{} Odd{}".format(even,odd))
print("Even {} Odd {}".format(even, odd))
print("Even : {} Odd : {}".format( even,odd))
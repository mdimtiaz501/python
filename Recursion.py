def recursion(x):
    print(x)
    if x == 0:
        return 1
    return x*recursion(x-1)

result = recursion(5)
recursion(5)
print(result)
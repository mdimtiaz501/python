def fibonacci(x):
    f = 1
    a = 0
    print(a)
    print(f)
    for i in range(2,x):
        c = a+f
        a = f
        f = c
        print(c)


fibonacci(8)
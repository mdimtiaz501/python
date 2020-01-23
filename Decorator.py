def say_hi(nam):
    return f"Hi, {nam}"

def greet_me(a_function):
    return a_function("Imtiaz")

print(greet_me(say_hi))

def divide(a,b):
    print(a/b)

def swap(div):
    def inside(a,b):
        if a<b:
            a,b = b,a
        return div(a,b)
    return inside

result = swap(divide)
result(6,8)
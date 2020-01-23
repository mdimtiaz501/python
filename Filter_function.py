from functools import reduce
number = [12,3,4,63,4,2,4,67,5,7,5,343,4,44,645,7,7,8,4]

def check_even(x):
    return x%2 == 0

even_nums = list(filter(check_even, number))
even_num = list(map(check_even, number))
adding = list(map(lambda n:n*3,even_nums))
print(even_nums)
print(even_num)
print(adding)

adding = reduce(lambda a,b:a+b,adding)
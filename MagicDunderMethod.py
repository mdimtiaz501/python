#python has some built in methods that do specific tasks. Those methods start and end with two underscore.

class MDM:
#    def __init__(self):
#        print("Hello world")

    def __str__(self):
        return "Hello world"


class MDM2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("Hello prithibi",self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        sumx = self.x + other.x
        sumy = self.y + other.y
        return sumx,sumy

    def __str__(self):
        print("Hey")
        return "Imtiaz"

    def __len__(self):
        print("okk")
        return len("Imtiaz")

obj = MDM()
obj2 = MDM2(5,6)
obj3 = MDM2(5,6)
obj4 = obj2+obj3

print(obj)
print(obj2==obj3)
print(obj4)
print('ImtiazChow'.__len__())
print(obj2)
print(len(obj2))


class A(object):
    def __new__(cls,x,y):
        cls.x = x
        cls.y = y
        print("Creating instance",cls.y)
        return super(A, cls).__new__(cls)

    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("Init is called")

    def __str__(self):
        return("Hello boys")

    def __len__(self):
        print(self.x+self.y)
        return len("Imtiaz")

    def text(self):
        print("Hello")


len(A(4,8))
print(len(A(1,1)))

A(2,5)

class AB():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("Init is called")

AB(7,9)

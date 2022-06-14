# class Computer:
#
#     def __init__(self):
#         self.name="amit"
#         self.age=19
#     #
#     # def update(self,):
#     #     self.age=20
#
#     def compare(self,other):
#         if self.age==other.age:
#             return True
#         else:
#             return False
#
#
# c1=Computer()
# c2=Computer()
# c1.age=30
#
# if c1.compare(c2):
#     print("same")
# else:
#     print("different")
#
# # c1.name="Sanket"
# # c1.age=12
#
# # c1.update()
#
# print(c1.name)
# print(c2.name)
# print(c1.age)

# ----------------------------------------

# class Car:
#
#     wheels=4
#
#     def __init__(self):
#         self.mil=10
#         self.com="BMW"
#
#
# c1=Car()
# c2=Car()
#
# Car.wheels=3
# c1.mil=23
#
# print(c1.com,c1.mil , c1.wheels)
# print(c2.com,c2.mil , c2.wheels)
#


# class Student:
#
#     school="Morgan"
#
#     def __init__(self, m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#
#     def avg(self):
#         return (self.m1+ self.m2 +self.m3)/3
#
#
# s1= Student(34,45,34)
# s2=Student(35,76,98)
#
# print(s1.avg())
#


# class Student:
#
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         self.lap=self.Laptop()
#
#     def show(self):
#         print(self.name , self.rollno)
#         self.lap.show()
#
#
#     class Laptop:
#
#         def __init__(self):
#             self.brand='hp'
#             self.cpu='i5'
#             self.ram= 8
#
#         def show(self):
#             print(self.brand,self.cpu,self.ram)
#
#
#
# s1=Student('Amit',2)
# s2=Student('Jenyy',3)
#
# s1.show()
#
#
#
#
# class A:
#
#     def __init__(self):
#         print(" in A init")
#
#     def feature1(self):
#         print("Feature 1 is working")
#
#     def feature2(self):
#         print("feature 2 is working")
#
#
# class B:
#
#     def feature3(self):
#         print("Feature 3 is working")
#
#     def feature4(self):
#         print("feature 4 is working")
#
#
# a=A()
# print= a.feature2()


# class Student():
#
#     def __init__(self , m1,m2):
#         if __name__ == '__main__':
#             self.m1=m1
#             self.m2=m2
#
#     def __add__(self, other):
#         m1=self.m1+self.m1
#         m2=self.m2+self.m2
#         s3=Student(m1,m2)
#         return s3
#
#     def __gt__(self, other):
#         r1=self.m1+self.m2
#         r2=other.m1+other.m2
#         if r1>r2:
#             return  True
#         else:
#             return
#
# s1=Student(34,56)
# s2=Student(23,67)
#
# s3=s1 + s2
#
# if s1>s2:
#     print("s1 wins")
# else:
#     print("s2 wins")



# ------------------------iterator

# class TopTen:
#
#     def __init__(self):
#         self.num=1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num<=10:
#             val= self.num
#             self.num+=1
#             return val
#         else:
#             raise StopIteration
#
#
# values=TopTen()
#
# for i in values:
#     print(i)

# -------------------genrators-------------------

def topten():

    n=1
    while n <=10:
        sq=n*n
        yield sq
        n=n+1

values =topten()

for i in values:
    print(i)
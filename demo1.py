# def add_sub(x,y):
#     c=x+y
#     d=x-y
#     return c,d
#
# r1,r2=add_sub(5,4)
# print(r1,r2)


# def data(name,age):
#     print(name)
#     print(age)
#
#
# data("amit", 23)
#
#
# def sum(a ,*b):
#
#     c=a
#     for i in b:
#         c=c+i
#
#     print(c)
# sum(2,3,5,2,4)


# def person(name,**data):
#     print(name)
#     print(data)
#
# person(name ='amit',age= 23, city='abad',mob='984342')
#
#
# def person(name,**data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
#
# person(name ='amit',age= 23, city='abad',mob='984342')

#
# def count(lst):
#     even=0
#     odd=0
#
#     for i in lst:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even, odd
# lst=[2,3,4,5,6,785,453,34,65,7,43,3,658,34]
# even,odd=count(lst)
# print(even)
# print(odd)

# ---------------------------fibonacci sequence----------------------

# def fib(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
#
# fib(5)

# ----------------------factorial of number-------

# def fact(x):
#     f=1
#
#     for i in range(1,x+1):
#         f=f*i
#
#     return f
#
#
#
# x=4
#
# result =fact(x)
#
# print(result)


# ------------------------lambda---------------------------

# f=lambda a,b : a+b
#
# result = f(5,6)
#
# print(result)

# nums = [3,5,6,2,6,8,6,94,79]
#
# evens = list (filter(lambda n: n%2==0,nums))
#
# doubles =list (map(lambda n: n*2,evens))
#
# print(evens)
# print(doubles)
# -------------------------------------------------------------------------------------


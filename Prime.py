
p=4

flag=False

if p>1:
    for i in range(2,p):
        print(i)
        if (p% i)==0:
            flag =True
            break

    if flag:
        print("not prime number")
    else:
        print("prime number")



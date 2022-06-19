# Python 3.x code to demonstrate star pattern

# pyramid pattern


def pypart(n):

    for i in range(0, n):


        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")


        print("\r")



n = 5
pypart(n)




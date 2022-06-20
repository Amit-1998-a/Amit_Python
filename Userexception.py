# define Python user-defined exceptions
class Error(Exception):

    pass


class ValueTooSmallError(Error):

    pass


class ValueTooLargeError(Error):

    pass


# you need to guess this number
number = 10

# user guesses a number until he gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")
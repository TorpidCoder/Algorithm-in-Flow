def fib(n):

    if(n<=1):
        return n

    return fib(n-1) + fib(n-2)

n = int(input("Enter the limit : "))

if(n<=0):
    print("Please enter a positive number")

else:
    print("Series is")

    for vals in range(0,n):
        print(fib(vals))


def fibseries(n):

    num1 = 0
    num2 = 1


    print(num1)
    print(num2)
    for vals in range(num2,n):
        num3 = num1+num2
        num1 = num2
        num2 = num3

        print (num3)
    return "Series"

print(fibseries(6))

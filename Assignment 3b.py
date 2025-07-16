def factorial(x):
    if(x <0):
        print("Enter a positive number ")
        return None
    elif (x<2):
        return 1

    return x * factorial (x-1)

number = int(input("Enter the number :  "))
result = factorial(number)
print("Factorial of ", number,"is :  ",result)
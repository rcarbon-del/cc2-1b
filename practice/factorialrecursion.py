def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
number = int(input("Enter number: "))
print(f"The factorial of {number} is {factorial(number)}.")
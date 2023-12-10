
def fib(count):
    if count == 0 or count == 1:
        return 1
    else:
        return fib(count - 1) + fib(count - 2)

    
count = int(input("Enter number: "))

print(fib(count))

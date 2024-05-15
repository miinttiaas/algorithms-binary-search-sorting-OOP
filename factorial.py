def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    elif n < 0:
        return "Factorial cannot be negative"
    else:
        return n * factorial(n-1)
print(factorial(4))
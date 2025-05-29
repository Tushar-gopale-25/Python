def factorial_recursive(n):
    if n == 0 or n == 1:  
        return 1
    return n * factorial_recursive(n - 1)  

number = 5
result = factorial_recursive(number)
print(f"The factorial of {number} is {result}")

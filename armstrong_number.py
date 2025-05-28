def is_armstrong(number):
    
    digits = str(number)
    num_digits = len(digits)
    total = sum(int(digit) ** num_digits for digit in digits)
    return total == number

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

def is_perfect(number):
    if number < 2:
        return False
    divisors_sum = 1  
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i
    return divisors_sum == number

num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

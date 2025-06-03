def is_palindrome(num):
    return str(num) == str(num)[::-1]

number = 121
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

import math

# Input numbers
a = 12
b = 18

# Calculate HCF (GCD)
hcf = math.gcd(a, b)

# Calculate LCM
lcm = abs(a * b) // hcf

print(f"HCF of {a} and {b} is: {hcf}")
print(f"LCM of {a} and {b} is: {lcm}")

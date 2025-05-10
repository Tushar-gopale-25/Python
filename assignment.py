a = 20
b = 10

a = b         # a = 10
print(a)      # 10

a += b        # a = 10 + 10 = 20
print(a)      # 20

a -= b        # a = 20 - 10 = 10
print(a)      # 10

a *= b        # a = 10 * 10 = 100
print(a)      # 100

a **= b       # a = 100 ** 10 = a large number
print(a)      # 100000000000000000000

a /= b        # a = large_number / 10 = float
print(a)      # 1e+21

a //= b       # a = 1e+21 // 10 = float (still)
print(a)      # 1e+20

a %= b        # a = 1e+20 % 10 = 0.0
print(a)      # 0.0

a &= b        
print(a)


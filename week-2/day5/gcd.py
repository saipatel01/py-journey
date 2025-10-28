a = 10
b = 15
small = min(a, b)
gcd = 1
for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("The GCD of", a, "and", b, "is", gcd)
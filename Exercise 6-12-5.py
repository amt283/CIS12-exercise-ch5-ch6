"""
The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.

One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b,
then gcd(a,b) = gcd(b,r). As a base case, we can use gcd(a, 0) = a.

Write a function called gcd that takes parameters a and b and returns their greatest common divisor.
"""

def gcd(a, b):
    # Continue the process until b becomes 0
    while b != 0:
        a, b = b, a % b  # Set a to b and b to the remainder of a divided by b
    return a  # When b becomes 0, a is the GCD

print(gcd(2,1)) # Should return 1
print(gcd(15,7)) # Should return 1
print(gcd(12,4)) # Should return 4
print(gcd(30,8)) # Should return 2
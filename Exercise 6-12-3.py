"""Write a boolean function, is_between(x, y, z),
that returns True if x < y < z or if z < y < x, and False otherwise."""

def is_between(x, y, z):
    if x < y < z or z < y < x:
        return True
    else:
        return False

print(is_between(1,2,3)) # True
print(is_between(7,5,2)) # True
print(is_between(13,2,13)) # False
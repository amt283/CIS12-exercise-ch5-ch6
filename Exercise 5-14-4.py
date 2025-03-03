"""Draw a stack diagram that shows the state of the program when it prints the result."""

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

"""Stack Diagram:

- recurse(3, 0) is called, n = 3, s = 0; since n != 0, the else statement runs with "3-1" and "3+0"
- recurse(2, 3) is called, n = 2, s = 3; since n != 0, the else statement runs with "2-1" and "2+3"
- recurse(1, 5) is called, n = 2, s = 5, since n != 0, the else statement runs with "1-1" and "1+5" 
- recurse(0, 6) is called, n = 0, s= 6; since n == 0, s is printed
"""
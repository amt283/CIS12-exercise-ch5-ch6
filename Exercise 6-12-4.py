"""
Write a function named ackermann that evaluates the Ackermann function.

What happens if you call ackermann(5, 5)?
"""

def ackermann(m, n):
    # Base case: when m == 0, return n + 1
    if m == 0:
        return n + 1
    # Recursive case 1: when m > 0 and n == 0, compute A(m-1, 1)
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    # Recursive case 2: when m > 0 and n > 0, compute A(m-1, A(m, n-1))
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(5,5)) # Causes RecursionError

"""
Useful information provided by ChatGPT:

Yes, calling ackermann(5, 5) with the original code would very likely cause a RecursionError.

Why?
-The Ackermann function grows extremely fast, and even for small values of m and n, it can cause deep recursion. 
Specifically:
-For ackermann(5, 5), the recursion depth would be extraordinarily large, requiring a massive number of recursive 
calls. The result would far exceed the default recursion depth limit of Python (which is 1000).

Key Points:
-Ackermann Function Growth: The Ackermann function's growth is so fast that even for values like ackermann(3, 4) or 
ackermann(4, 2), Python might hit the recursion depth limit. For ackermann(5, 5), the function would require many 
more recursive calls, and Python's default recursion limit will almost certainly be exceeded.
-Default Recursion Limit: Python's default recursion limit is 1000, which is generally enough for most recursive 
functions, but the Ackermann function's recursive depth is much larger, especially when the inputs are high.

How to Mitigate It:
-You can increase the recursion limit using sys.setrecursionlimit(), but be cautious when 
doing so, as too large a value can lead to a stack overflow or crash your program if the system's resources 
are exhausted."""
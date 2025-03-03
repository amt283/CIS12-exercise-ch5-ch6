"""Write a function named is_triangle that takes three integers as arguments, and that prints either “Yes” or “No”,
depending on whether you can or cannot form a triangle from sticks with the given lengths.
Hint: Use a chained conditional."""

"""If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, 
you can. (If the sum of two lengths equals the third, they form what is called a “degenerate” triangle.)"""

def is_triangle(side_a, side_b, side_c):
    # Chained conditional to test the triangle sides
    if (side_a + side_b > side_c
            and side_a + side_c > side_b
            and side_b + side_c > side_a):
        print("Yes")
    else:
        print("No")

    # Example usage:

is_triangle(12, 1, 1) # Fail
is_triangle(7, 4, 6)  # Pass
is_triangle(2, 3, 14)  # Fail
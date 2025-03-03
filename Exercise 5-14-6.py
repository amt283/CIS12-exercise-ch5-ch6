"""To draw a Koch curve with length x, all you have to do is

1. Draw a Koch curve with length x/3.
2. Turn left 60 degrees.
3. Draw a Koch curve with length x/3.
4. Turn right 120 degrees.
5. Draw a Koch curve with length x/3.
6. Turn left 60 degrees.
7. Draw a Koch curve with length x/3.
The exception is if x is less than 5 – in that case, you can just draw a straight line with length x.

Write a function called koch that takes x as an argument and draws a Koch curve with the given length."""

import turtle

def main():
    make_turtle(delay=0)
    koch(120)
    turtle.done()


def make_turtle(delay=0):
    # Set up the screen and turtle
    screen = turtle.Screen()
    screen.title("Koch Curve")

    # Create a turtle
    t = turtle.Turtle()
    t.shape("triangle")
    t.speed(0)  # Fastest drawing speed

    # Set the delay between drawing steps
    screen.delay(delay)

    return t


def koch(x):
    """Draw a Koch curve with length 'x'."""
    t = make_turtle()  # Create the turtle inside the koch function
    if x < 5:
        t.forward(x)  # If the length is less than 5, just draw a straight line
    else:
        # Recursive part
        # Draw the first part of the curve (length x/3)
        koch_recursive(t, x / 3)
        t.left(60)  # Turn left 60 degrees

        # Draw the second part of the curve (length x/3)
        koch_recursive(t, x / 3)
        t.right(120)  # Turn right 120 degrees

        # Draw the third part of the curve (length x/3)
        koch_recursive(t, x / 3)
        t.left(60)  # Turn left 60 degrees

        # Draw the last part of the curve (length x/3)
        koch_recursive(t, x / 3)


def koch_recursive(t, x):
    """Helper function for the recursive drawing of the Koch curve."""
    if x < 5:
        t.forward(x)  # If the length is less than 5, just draw a straight line
    else:
        koch_recursive(t, x / 3)
        t.left(60)
        koch_recursive(t, x / 3)
        t.right(120)
        koch_recursive(t, x / 3)
        t.left(60)
        koch_recursive(t, x / 3)

if __name__ == "__main__":
    main()

"""Useful info provided by the VA:
    
Explanation of Changes:
-koch(x):
--The main koch function now only takes one argument x, the length of the Koch curve to be drawn.
--Inside koch(x), the turtle is created by calling make_turtle() and stored in the variable t.
--If the length x is less than 5, it simply draws a straight line with t.forward(x).
--Otherwise, it calls a helper function koch_recursive(t, x / 3) to perform the recursive drawing of the Koch curve.

-koch_recursive(t, x):
--This is a helper function that does the actual recursive drawing of the Koch curve.
--It works similarly to the previous implementation, but now the turtle object t is passed as an argument to the helper 
function.
--It handles the recursion by dividing the length x by 3 and applying the turns as described.

Key Changes:
-Single argument x: Now, koch(x) is the only function that takes one positional argument (x), which is the length of 
the Koch curve.
-Helper function (koch_recursive): The recursion logic is moved to a separate helper function koch_recursive to avoid 
passing the turtle object through each recursive call.

Example Usage:
When you call koch(120), the turtle will draw the Koch curve with an initial length of 120, using the recursive 
procedure outlined in the koch_recursive function.

Keeping the window open:
After the drawing is complete, turtle.done() ensures that the drawing window remains open until you close it.

Result:
The program will draw a Koch curve fractal based on the length x you pass in the koch() function. The curve becomes more intricate with higher values of x and depth of recursion.
"""
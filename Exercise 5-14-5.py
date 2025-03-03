"""
Read the following function and see if you can figure out what it does. Then run it and see if you got it right.
Adjust the values of length, angle and factor and see what effect they have on the result. If you are not
sure you understand how it works, try asking a virtual assistant.

"""

from turtle import forward, left, right, back


def draw(length):
    angle = 50
    factor = 0.6

    if length > 5:
        forward(length)
        left(angle)
        draw(factor * length)
        right(2 * angle)
        draw(factor * length)
        left(angle)
        back(length)

#draw(50)
#draw(4)
draw(10)

"""Prediction: it's going to draw the capital letter R
Result: I wasn't even close! :P I didn't connect the dots that the "right(2 * angle)" meant the turtle was 
turning around
"""


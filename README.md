# CIS 12, Chapters 5 and 6 Exercises

<h2>Chapter 5 Reflection</h2>

- <b>Exercise 5-14-2</b>
Compared to the instructor's version, I think it's a bit of a toss up regarding which version is better depending 
on what you want the program to do. For example, I can see the benefit of putting everything in functions/generalizing 
like the instructor does because it's much more efficient and allows code to be reused without wasting lines of code, 
but is generalizing important if you're doing one thing (ex: finding seconds from 1970 to now) or the program is 
already pretty short? Is it just a case of it's a good idea to get into the practice of generalizing regardless of 
program length so you'll develop good habits?

If this is the case, then I'd say the instructor's code is the better version. If not, then I'd say I like my 
version a teensy bit better only because it's easier for me to follow along and understand what's happening (though 
that's partly because I wrote it and partly because I don't fully understand all the built-in math/time functions 
that were used in the instructor-version)

- <b>Exercise 5-14-3</b>
My version looks pretty close to the instructors, more or less, so there's not much to compare. :)

- <b>Exercise 5-14-4</b>
My version looks pretty close to the instructors, more or less, so there's not much to compare. :)

- <b>Exercise 5-14-5</b>
This was a prediction exercise, so there's not much to compare. I tried to draw out what path I thought the turtle 
would take based on the steps in the draw() function, but I misunderstood the "right(2 * angle)" line, which I'm pretty 
sure lets the turtle turn around and helps create the honeycomb shape and that's what I thought was a very angular "R".

- <b>Exercise 5-14-6</b>
This one was a tough one, I couldn't figure it out and I ended up having to ask ChatGPT to give me a hand making the
program because I wanted to see what it would come up with/see a breakdown of why it chose to do certain things. For
this reason, I'd have to say that the instructor's version is much better by default. The biggest thing that threw me
(outside of struggling with recursion and math in general :P ) is that the example in the book indicated that "koch()" 
would have one positional argument but if I needed to have make_turtle() be a separate function then koch() needed 
to have two positional arguments to pass t from make_turtle() to koch() - like what was done in the instructor's 
version. So, I think I was trying to follow the book a little too closely. :)

<h2>Chapter 6 Reflection</h2>

- <b>Exercise 6-12-2</b>
My version looks pretty close to the instructors, more or less, so there's not much to compare. :)

- <b>Exercise 6-12-3</b>
My version looks pretty close to the instructors, though the instructor's version is much more concise by condensing
the return statement down to boolean value generated from "(x < y < z) or (z < y < x)" so I think it's the better one.

- <b>Exercise 6-12-4</b>
This was another one I couldn't figure out and ended up asking ChatGPT for help, so I could follow along and understand 
the process. I still don't fully understand the process behind the Ackermann function, but at least now I can follow
the steps. I also found it interesting to see how the recursion caused the arguments, which started off small,
to grow wildly to the point of crashing the program altogether

- <b>Exercise 6-12-5</b>
My version looks pretty close to the instructors, more or less, so there's not much to compare. :)
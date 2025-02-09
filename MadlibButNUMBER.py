#Testing FSTRING

number = int(input("Pick your number. "))

madlib = f"""
Based on your number {number}, we can get the floating point {0.1234 + number:.2f}. {number} also can be represent in hexadecimal which is {number:X}. 
Then we can even make a binary representation {number:b}. In addition, your number can be shown as {number:b} octal format, 
{number:E} scientific format, {number:+} positive sign, {-number} negative sign and finally even in percentage {number/100:.0%} .
Hence concluded, after python 3.6, we can safely said fstring is better in most case scenario after format() and %-old style format  """

madlib_2 = f"""
As a space explorer, Sally discovered a planet {number} light-years away. 
Her spaceship's computer calculated the distance as {number:.2f} parsecs, but the alien map showed it as {number:b} in their binary system. 
The alien ambassador said, "Our planet's energy output is {number:x} zettaflops, and our civilization is {number:E} years old." 
She adjusted her course by {+number:+} degrees and {-number:-} light-years, achieving {number:.0%} mission success.
"""

madlib_3 = f"""
Bobby bough a groceries worth a {number} $, then he looked through the receipt and found missing {number:.2f} items. 
He went back to cashier to ask {number:b} questions. The cashier stated the problem lies in {number:E} of the program. 
The cashier improvised the codes by making {+number:+} and {-number:-} of steps and overall achieve {number:.0%} of efficiency."""

madlib_4 = f"""
In a mysterious library, you found a book with {number} pages. 
The librarian said, "This book is {number:.2f}% complete, but it's missing {number:b} chapters." 
You opened the book and saw a formula: E = mc^{number:x}, which looked like a secret code. 
The librarian whispered, "The truth lies in {number:E} of the universe." 
You left the library feeling {+number:+}% inspired and {-number:-}% confused, but overall, you achieved {number:.0%} clarity.
"""
madlib_5 = f"""
Barbara found a magical potion labeled "Strength {number}." 
The recipe called for {number:.2f} drops of moonlight and {number:b} grams of stardust. 
The potion's instructions said, "Mix at {number:x} RPM and heat to {number:E} degrees." 
Barbara drank it and felt {+number:+}% stronger and {-number:-}% sleepier, but overall, she achieved {number:.0%} of her potential.
"""

madlib_6 = f"""
A time traveler appeared and said, "I come from the year {number}." 
They showed you a device that could travel at {number:.2f} times the speed of light. 
The device's manual was written in binary: {number:b}, and its energy source was {number:x} joules. 
The traveler explained, "The future is {number:E} years away, but with this device, you can reach it in {+number:+} steps or {-number:-} leaps." 
You asked, "What are the odds of success?" They replied, "{number:.0%} guaranteed."
"""

madlib_7 = f"""
Toby cracked a secret code: {number}. 
The decoder revealed that the message was {number:.2f}% encrypted and contained {number:b} hidden words. 
The code's metadata said, "Created on {number:x}-{number:E} by Agent X." 
Toby followed the trail {+number:+} steps forward and {-number:-} steps back, uncovering {number:.0%} of the mystery.
"""

print(madlib)
print(madlib_2)
print(madlib_3)
print(madlib_4)
print(madlib_5)
print(madlib_6)
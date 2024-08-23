for x in range (0,10):
    x = x // 3
    print(x)

for y in range (0,10):
    y = y % 3
    print(y)


#WOW mind blown LMAO
#So we can use int // any value to get the row index, which you can use to determine where the user currently at
#as we can see, it will divide by 3 for 012 which = 0, that's for index 0
#later 345, = 1 ... and 678 = 2
# so x or int() is the user input, divide by any value equivalent to num of items in row
# hence it will iterate over that items... got me? lol

#Another MIND BLOWN
#LOL
#We can get the Column INDEX if we use replace // with %
#just try it out, like in the above, for 012, the remainder you will see it return..-
# 012 as 0 / 3 = 0 (no remainder), 1/3 = 1 remainder and goes on...
# so you will see it like give index over column with reference to item of row but 0 as default

# additional note. using // can give round off answer instead of just / which give floating point if there is.



# Another trick of %
# trick? wtv . logic... yes that the correct word.
# any (int % 2 == 0) is used to get even number and vice versa if not equal to 0

    lalala = [z for z in range (0,10) if z % 2 == 0 ]
    print(lalala)


#testing all()


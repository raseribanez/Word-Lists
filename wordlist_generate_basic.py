#!/usr/bin/env/python
# Ben Woodfield - Written and tested on Python 2.7
# Generates ALL possible letter combos of 'abc', WITHOUT using the same letters
# more than once

# Change: 'abcdefg' to include your own paramaters and characters
# Change: repeat=8 - 8 is the number of letters in each word it returns
import itertools
res = itertools.permutations('abcdefg',8)
for i in res: 
   print ''.join(i)

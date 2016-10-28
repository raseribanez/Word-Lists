#!/usr/bin/env/python
# Ben Woodfield
# An upgrade to wordlist_generate.py This version allows the user
# to select 2 values to return: a minimum word length and a maximum word length

import itertools

chrs = 'abc123' # 'abc123' are the set of characters to include in the results
min_length, max_length = 2, 5 #(2 is min word-length)(5 is max word-length)   
for n in range(min_length, max_length+1):
    for xs in itertools.product(chrs, repeat=n):
        print ''.join(xs)

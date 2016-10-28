#!/usr/bin/env/python
# Ben Woodfield
# Another way to generate a wordlist
# By building a function, you can call the generator into any script

from itertools import product

def allwords(chars, length):
    for letters in product(chars, repeat=length):
        yield ''.join(letters)

def main():
    letters = "abc123"
    for wordlen in range(3, 5):
        for word in allwords(letters, wordlen):
            print(word)

if __name__=="__main__":
    main()

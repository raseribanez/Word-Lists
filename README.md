# Word-Lists
Some basic wordlists - and wordlist generators

Now some of the words.txt documents arent done using my Python wordlist generator - they are lists of actual
words - from a dictionary and created for a Scrabble game.

My Python Wordlist Generators dont create actual words...but they do create EVERY possible combination of
characters based on the paramaters you provide.

To use the Python wordlist generators you just need Python 2.7 - I haven't tried them with Py3 yet
They work as follows:

wordlist_generator_basic.py - generates every possible combination of given characters - at a given word-length.
(Does NOT allow the repeat use of characters in each word - characters can only be used ONCE for each word - Prints 
results to the Shell Window)

wordlist_generator.py  -  generates every possible combination of given characters - at a given word-length.
(Allows the repeat use of characters in results - characters can be used more than once in each word -Prints 
results to the Shell Window )

wordlist_generate_function.py - Same as above but written into a function. Idea was to be able to call it into other programs

wordlist_to_txt_generator.py - This version prints results to a new Text document and asks the user to enter the filename desired
(The txt document with the wordlist inside will be saved in the SAME directory as the generator script is saved in)



NOTE: I apologise if one or two of the wordlist related documents here also appear in my other repository
I decided it was more practical to have a seperate repository for the wordlists alone
as they can be used for a much wider range of applications than pen-testing. So I have created the repo
for my wordlist related oftware, and will re-organize the pen-testing one as and when I feel the need to!

Also one of these wordlists were taken from a scrabble game! yes a scrabble game, it is a FULL list of the English 
dictionary. May be of use, but I was using it as an example for another application (game development idea)

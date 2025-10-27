"""
Ask for word

Cheer each letter

Example:
Give me a word: Tax
Give me ....
Give me ....
Give me ...

NB: Rules of english apply
Vowel letters must be with 'an' -> AEIOU
"""

vowels = ('a','e','i','o','u')

word = input("Give me a word: ")

max_letters=len(word)
counter = 0
while(counter<max_letters):
    if(word[counter].lower() in vowels):
        print(f"Give me an {word[counter]} !!!")
    else:
        print(f"Give me a {word[counter]} !!!")
    counter += 1
"""
for char in word:
    (if char.lower() in vowels:
        print....,
    else:
        ...
"""
Words = input()
Alphabet = "abcdefghijklmnopqrstuvwxyz"

if sum([Words in Alphabet]) < (len(Words)+1) / 2:
    print(Words.upper())
else:
    print(Words.lower())


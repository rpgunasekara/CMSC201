"""
File: detector.py
Author: Ravindu Gunasekara
Date: 09/25/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Asks for a word and searches
    through the word for a diphthong,
    printing the number of diphthongs
    after.
"""
diphthong = input("Tell me a word you wish to check for diphthongs: ").lower()
vowel = ["a", "e", "i", "o", "u", "y"]
split_diphthong = list()
count = 0

for i in range(len(diphthong) - 1):
    if diphthong[i] in vowel and diphthong[i + 1] in vowel:
        count += 1
    if diphthong[i] == 'u' and diphthong[i - 1] == 'q':
        count -= 1

print(f"There is/are {count} diphthong(s) in the string.")
